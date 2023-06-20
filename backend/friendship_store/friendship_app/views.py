from rest_framework import generics
from rest_framework.views import APIView, Response
import friendship_app.models as model
import friendship_app.serializers as fs
from django.db.models import Q
from django.http import Http404, JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from friendship_app.tasks import order_notice
from django.core.exceptions import ObjectDoesNotExist


class SearchAPIView(generics.ListAPIView):
    """
    Представление API для поиска продуктов на основе заданного слова.
    """
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        """
        Возвращает набор объектов запроса (queryset) продуктов, отфильтрованных на основе заданного слова (`word`).
        Поиск осуществляется по нескольким полям продукта, включая название продукта (`product_name`),
        модель (`model`), категорию (`category_name`) и бренд (`brand_name`).
        Если ничего не найдено, возбуждается исключение `Http404` с сообщением об ошибке.
        """
        word = self.kwargs['word'].lower()

        queryset = model.Product.objects.filter(
            Q(product_name__icontains=word) |
            Q(model__icontains=word) |
            Q(category__category_name__icontains=word) |
            Q(brand__brand_name__icontains=word)
        )

        if not queryset.exists():
            raise Http404(f'Ничего не нашлось по запросу "{word}"')

        return queryset

    def list(self, request, *args, **kwargs):
        """
        Переопределенный метод `list()`, вызывающий родительскую реализацию метода `list()` для получения списка продуктов.
        Если возникает исключение `Http404`, возвращается JSON-ответ с сообщением об ошибке и статусом 404.
        """
        try:
            return super().list(request, *args, **kwargs)
        except Http404 as e:
            return JsonResponse({'error': str(e)}, status=404)


class ProductAPIView(generics.ListAPIView):
    """
    Представление API для получения списка всех продуктов.
    """
    queryset = model.Product.objects.all()
    serializer_class = fs.ProductSerializer


class ProductByIdAPIView(APIView):
    """
    Представление API для получения информации о продукте по его идентификатору.
    """

    def get(self, request, product):
        """
        Возвращает информацию о продукте с заданным идентификатором (`product`).
        Включает данные о продукте, отзывы и изображения, связанные с этим продуктом.
        """
        product = model.Product.objects.get(model=product)
        reviews = model.Review.objects.filter(product_id=product.id)
        images = model.Image.objects.filter(product_id=product.id)
        response_data = {
            'product': fs.ProductSerializer(product).data,
            'review': [fs.ReviewSerializer(review).data for review in reviews],
            'images': [fs.ImageSerializer(image).data for image in images],
        }
        return Response(response_data)


class ProductByCategoryAPIView(generics.ListAPIView):
    """
    Представление API для получения списка продуктов по категории с возможностью фильтрации и сортировки.
    """
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        """
        Возвращает набор объектов запроса (queryset) продуктов, отфильтрованных по заданной категории и опциональным
        параметрам фильтрации и сортировки.
        """
        category = self.kwargs['category']
        queryset = model.Product.objects.filter(category__category_name=category)
        min_price = self.request.query_params.get('min_price', 0)
        max_price = self.request.query_params.get('max_price', 999_999_999)
        sort_by = self.request.query_params.get('sort_by', 'incr')

        # Применение фильтрации по цене
        queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        # Применение сортировки
        if sort_by == 'incr':
            queryset = queryset.order_by('price')
        elif sort_by == 'decr':
            queryset = queryset.order_by('-price')

        return queryset


class ProductByBrandAPIView(generics.ListAPIView):
    """
    Представление API для получения списка продуктов по бренду с возможностью фильтрации и сортировки.
    """
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        """
        Возвращает набор объектов запроса (queryset) продуктов, отфильтрованных по заданному бренду и опциональным
        параметрам фильтрации и сортировки.
        """
        brand = self.kwargs['brand']
        queryset = model.Product.objects.filter(brand__brand_name=brand)
        min_price = self.request.query_params.get('min_price', 0)
        max_price = self.request.query_params.get('max_price', 999_999_999)
        sort_by = self.request.query_params.get('sort_by', 'incr')

        # Применение фильтрации по цене
        queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        # Применение сортировки
        if sort_by == 'incr':
            queryset = queryset.order_by('price')
        elif sort_by == 'decr':
            queryset = queryset.order_by('-price')

        return queryset


class CategoryAPIView(generics.ListAPIView):
    """
    Класс API для получения списка всех категорий.
    """
    queryset = model.Category.objects.all()
    serializer_class = fs.CategorySerializer


class FavoriteListAPIView(generics.ListAPIView):
    """
    Представление API для получения списка избранных элементов пользователя.
    """
    serializer_class = fs.FavoriteGetSerializer

    def get_queryset(self):
        """
        Возвращает набор объектов запроса (queryset) избранных элементов пользователя, отфильтрованных по заданному токену.
        """
        token = self.kwargs['token']
        user_id = Token.objects.get(key=token).user_id
        return model.Favorite.objects.filter(user_id=user_id)


class FavoriteCreateAPIView(generics.CreateAPIView):
    """
    Представление API для создания элемента в избранном.
    """
    serializer_class = fs.FavoriteSerializer

    def perform_create(self, serializer):
        """
        Выполняет создание элемента в избранном, сохраняя связь с соответствующим пользователем и проверяя дублирование.
        """
        data = serializer.validated_data
        user_id = Token.objects.get(key=data['token']).user_id
        data['user_id'] = User.objects.get(id=user_id)
        del data['token']

        favorite = model.Favorite.objects.filter(product_id=data['product_id'], user_id=user_id)
        if favorite.exists():
            raise ValidationError({'error': 'Товар уже добавлен в избранное.'})

        serializer.save()


class FavoriteDestroyAPIView(generics.DestroyAPIView):
    """
    Представление API для удаления элемента из избранного.
    """
    serializer_class = fs.FavoriteSerializer

    def get_queryset(self):
        """
        Возвращает набор объектов запроса (queryset) элемента избранного, отфильтрованных по заданному идентификатору.
        """
        pk = self.kwargs['pk']
        return model.Favorite.objects.filter(id=pk)


class BrandAPIView(generics.ListAPIView):
    """
    Представление API для получения списка всех брендов.
    """
    queryset = model.Brand.objects.all()
    serializer_class = fs.BrandSerializer


class AlbumAPIView(generics.ListAPIView):
    """
    Представление API для получения списка всех альбомов.
    """
    queryset = model.Album.objects.all()
    serializer_class = fs.AlbumSerializer


class AddToBasketAPIView(generics.CreateAPIView):
    """
    Представление API для добавления товара в корзину.
    """
    serializer_class = fs.BasketPostSerializer

    def perform_create(self, serializer):
        """
        Выполняет добавление товара в корзину, уменьшение количества товара и обработку исключений.
        """
        data = serializer.validated_data
        product_id = data['product_id'].id

        try:
            user_id = Token.objects.get(key=data['token']).user_id
            data['user_id'] = User.objects.get(id=user_id)
            product = model.Product.objects.get(id=product_id)
        except ObjectDoesNotExist as e:
            raise ValidationError({'error': str(e)})

        del data['token']

        if product.quantity > 0:
            product.quantity -= 1
            product.save()
        else:
            product.availability = False
            product.save()
            raise ValidationError({'error': 'Товара нет в наличии.'})

        try:
            basket = model.Basket.objects.get(product_id=product_id, ordered=False)
            basket.quantity += 1
            basket.save()
        except ObjectDoesNotExist:
            serializer.save()

    def get_queryset(self):
        """
        Возвращает набор объектов запроса (queryset).
        """
        return self.queryset


class BasketGetAPIView(APIView):
    """
    Представление API для получения содержимого корзины пользователя.
    """

    def get(self, request, token):
        """
        Возвращает содержимое корзины пользователя и общую стоимость товаров.
        """
        user_id = Token.objects.get(key=token).user_id
        basket = model.Basket.objects.filter(user_id=user_id, ordered=False)
        total_price = sum([b.product_id.price * b.quantity for b in basket])

        response_data = {
            'basket': [fs.BasketGetSerializer(b).data for b in basket],
            'total_price': total_price,
        }

        return Response(response_data)


class BasketQuantityAPIView(APIView):
    """
    Представление API для изменения количества товара в корзине.
    """

    def get(self, request, basket_id, incr):
        """
        Изменяет количество товара в корзине, и обновляет количество товара в наличии.
        """
        try:
            basket = model.Basket.objects.get(id=basket_id, ordered=False)
        except ObjectDoesNotExist:
            return Response({'error': 'Такой корзины не существует.'}, status=400)

        product = model.Product.objects.get(id=basket.product_id.id)

        if incr == 'incr':
            if product.quantity <= 0:
                product.availability = False
                product.save()
                return Response({'error': 'Товара нет в наличии.'}, status=400)
            basket.quantity += 1
            product.quantity -= 1
        elif incr == 'decr':
            basket.quantity -= 1
            product.quantity += 1
            if basket.quantity == 0:
                basket.delete()
                return Response({'message': 'Товар удален из корзины.'}, status=200)
        basket.save()
        product.save()

        return Response({'message': 'Количество товара в корзине обновлено.'}, status=200)


class OrderAPIView(generics.CreateAPIView):
    """
    Представление API для создания заказа.
    """
    serializer_class = fs.OrderSerializer

    def perform_create(self, serializer):
        """
        Создает заказ и обрабатывает связанные действия.
        """
        data = serializer.validated_data
        user_id = Token.objects.get(key=data['token']).user_id
        data['user_id'] = User.objects.get(id=user_id)

        basket = model.Basket.objects.filter(user_id=user_id, ordered=False)

        if not basket.exists():
            raise ValidationError({'error': 'Корзина пустая.'})

        total_price = 0
        for b in basket:
            b.ordered = True
            total_price += b.quantity * b.product_id.price
            b.save()

        data['total_price'] = total_price
        del data['token']

        first_name = User.objects.get(id=user_id).first_name
        email = User.objects.get(id=user_id).email
        order_notice.delay(first_name, total_price, email)

        serializer.save()


class NewsAPIView(generics.ListAPIView):
    """
    Представление API для получения списка новостей.
    """
    queryset = model.News.objects.all()
    serializer_class = fs.NewsSerializer


class CreateReviewAPIView(generics.CreateAPIView):
    """
    Представление API для создания отзыва.
    """
    serializer_class = fs.ReviewSerializer

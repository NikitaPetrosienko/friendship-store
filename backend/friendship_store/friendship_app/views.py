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


class SearchAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
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
        try:
            return super().list(request, *args, **kwargs)
        except Http404 as e:
            return JsonResponse({'error': str(e)}, status=404)


class ProductAPIView(generics.ListAPIView):
    queryset = model.Product.objects.all()
    serializer_class = fs.ProductSerializer


class ProductByIdAPIView(APIView):
    def get(self, request, product):
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
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        queryset = model.Product.objects.filter(category__category_name=category)
        min_price = self.request.query_params.get('min_price', 0)
        max_price = self.request.query_params.get('max_price', 999_999_999)
        sort_by = self.request.query_params.get('sort_by', 'incr')
        queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        if sort_by == 'incr':
            queryset = queryset.order_by('price')
        elif sort_by == 'decr':
            queryset = queryset.order_by('-price')
        return queryset


class ProductByBrandAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        brand = self.kwargs['brand']
        queryset = model.Product.objects.filter(brand__brand_name=brand)
        min_price = self.request.query_params.get('min_price', 0)
        max_price = self.request.query_params.get('max_price', 999_999_999)
        sort_by = self.request.query_params.get('sort_by', 'incr')
        queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        if sort_by == 'incr':
            queryset = queryset.order_by('price')
        elif sort_by == 'decr':
            queryset = queryset.order_by('-price')
        return queryset


class CategoryAPIView(generics.ListAPIView):
    queryset = model.Category.objects.all()
    serializer_class = fs.CategorySerializer


class FavoriteListAPIView(generics.ListAPIView):
    serializer_class = fs.FavoriteGetSerializer

    def get_queryset(self):
        token = self.kwargs['token']
        user_id = Token.objects.get(key=token).user_id
        return model.Favorite.objects.filter(user_id=user_id)


class FavoriteCreateAPIView(generics.CreateAPIView):
    serializer_class = fs.FavoriteSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        user_id = Token.objects.get(key=data['token']).user_id
        data['user_id'] = User.objects.get(id=user_id)
        del data['token']
        serializer.save()


class FavoriteDestroyAPIView(generics.DestroyAPIView):
    serializer_class = fs.FavoriteSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return model.Favorite.objects.filter(id=pk)


class BrandAPIView(generics.ListAPIView):
    queryset = model.Brand.objects.all()
    serializer_class = fs.BrandSerializer


class AlbumAPIView(generics.ListAPIView):
    queryset = model.Album.objects.all()
    serializer_class = fs.AlbumSerializer


class AddToBasketAPIView(generics.CreateAPIView):
    serializer_class = fs.CreateBasketSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        user_id = Token.objects.get(key=data['token']).user_id
        data['user_id'] = User.objects.get(id=user_id)
        del data['token']
        product = model.Product.objects.get(id=data['product_id'].id)
        product.quantity -= 1

        if product.quantity >= 0:
            product.save()
            serializer.save()
        else:
            raise ValidationError('Товара нет в наличие.')

    def get_queryset(self):
        return self.queryset


class GetBasketAPIView(APIView):
    def get(self, request, token):
        user_id = Token.objects.get(key=token).user_id
        basket = model.Basket.objects.filter(user_id=user_id, ordered=False)
        total_price = sum([b.product_id.price * b.quantity for b in basket])
        response_data = {
            'basket': [fs.GetBasketSerializer(b).data for b in basket],
            'total_price': total_price,
        }
        return Response(response_data)


class OrderAPIView(generics.CreateAPIView):
    serializer_class = fs.OrderSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        user_id = Token.objects.get(key=data['token']).user_id
        data['user_id'] = User.objects.get(id=user_id)

        basket = model.Basket.objects.filter(user_id=user_id)

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
    queryset = model.News.objects.all()
    serializer_class = fs.NewsSerializer


class CreateReviewAPIView(generics.CreateAPIView):
    serializer_class = fs.ReviewSerializer

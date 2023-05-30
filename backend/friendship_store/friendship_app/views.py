from rest_framework import generics
from rest_framework.views import APIView, Response
import friendship_app.models as model
import friendship_app.serializers as fs
from django.db.models import Q
from django.http import Http404, JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


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
        return model.Product.objects.filter(category__category_name=category)


class ProductByBrandAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        brand = self.kwargs['brand']
        return model.Product.objects.filter(brand__brand_name=brand)


class CategoryAPIView(generics.ListAPIView):
    queryset = model.Category.objects.all()
    serializer_class = fs.CategorySerializer


class FavoriteListAPIView(generics.ListAPIView):
    serializer_class = fs.FavoriteGetSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
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
        product.quantity -= int(data['quantity'])

        if product.quantity >= 0:
            product.save()
            serializer.save()
        else:
            raise ValidationError('Товара нет в наличие.')

    def get_queryset(self):
        return self.queryset


class BasketByIdAPIView(generics.ListAPIView):
    serializer_class = fs.CreateBasketSerializer

    def get_queryset(self):
        token = self.kwargs['token']
        user_id = Token.objects.get(key=token).user_id
        return model.Basket.objects.filter(user_id=user_id)


class NewOrderAPIView(generics.CreateAPIView):
    serializer_class = fs.OrderSerializer


class NewsAPIView(generics.ListAPIView):
    queryset = model.News.objects.all()
    serializer_class = fs.NewsSerializer


class CreateReviewAPIView(generics.CreateAPIView):
    serializer_class = fs.ReviewSerializer

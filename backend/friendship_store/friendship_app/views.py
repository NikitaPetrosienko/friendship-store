from rest_framework import generics
from rest_framework.views import APIView, Response
import friendship_app.models as model
import friendship_app.serializers as fs


class ProductAPIView(generics.ListAPIView):
    queryset = model.Product.objects.all()
    serializer_class = fs.ProductSerializer


class ProductByIdAPIView(APIView):
    def get(self, request, product_id):
        product = model.Product.objects.get(id=product_id)
        reviews = model.Review.objects.filter(product_id=product_id)
        images = model.Image.objects.filter(product_id=product_id)
        response_data = {
            'product': fs.ProductSerializer(product).data,
            'review': [fs.ReviewSerializer(review).data for review in reviews],
            'images': [fs.ImageSerializer(image).data for image in images],
        }
        return Response(response_data)


class ProductByCategoryAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category_id']
        return model.Product.objects.filter(category=category)


class ProductByBrandAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        brand = self.kwargs['brand_id']
        return model.Product.objects.filter(brand=brand)


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
    serializer_class = fs.BasketSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        product = model.Product.objects.get(id=data['product_id'].id)
        product.quantity -= int(data['quantity'])

        if product.quantity >= 0:
            product.save()
            serializer.save()


class BasketByIdAPIView(generics.ListAPIView):
    serializer_class = fs.BasketSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return model.Basket.objects.filter(user_id=user_id)


class NewOrderAPIView(generics.CreateAPIView):
    serializer_class = fs.OrderSerializer


class NewsAPIView(generics.ListAPIView):
    queryset = model.News.objects.all()
    serializer_class = fs.NewsSerializer


class CreateReviewAPIView(generics.CreateAPIView):
    serializer_class = fs.ReviewSerializer

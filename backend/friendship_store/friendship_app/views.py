from rest_framework import generics

import friendship_app.models as model
import friendship_app.serializers as fs


class ProductAPIView(generics.ListAPIView):
    queryset = model.Product.objects.all()
    serializer_class = fs.ProductSerializer


class ProductByIdAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return model.Product.objects.filter(id=product_id)


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


class BrandAPIView(generics.ListAPIView):
    queryset = model.Brand.objects.all()
    serializer_class = fs.BrandSerializer


class AlbumAPIView(generics.ListAPIView):
    queryset = model.Album.objects.all()
    serializer_class = fs.AlbumSerializer


class ImageAPIView(generics.ListAPIView):
    serializer_class = fs.ImageSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return model.Image.objects.filter(product_id=product_id)


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


class ReviewAPIView(generics.ListAPIView):
    serializer_class = fs.ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return model.Review.objects.filter(product_id=product_id)


class CreateReviewAPIView(generics.CreateAPIView):
    serializer_class = fs.ReviewSerializer

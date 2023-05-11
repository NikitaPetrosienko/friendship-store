from rest_framework import generics

from friendship_app.models import Product, Category, Brand, Basket
import friendship_app.serializers as fs


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = fs.ProductSerializer


class ProductByIdAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['id']
        return Product.objects.filter(id=product_id)


class ProductByCategoryAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)


class ProductByBrandAPIView(generics.ListAPIView):
    serializer_class = fs.ProductSerializer

    def get_queryset(self):
        brand = self.kwargs['brand']
        return Product.objects.filter(brand=brand)


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = fs.CategorySerializer


class BrandAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = fs.BrandSerializer


class AddToBasketAPIView(generics.CreateAPIView):
    serializer_class = fs.BasketSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        product = Product.objects.get(id=data['product_id'].id)
        product.quantity -= int(data['quantity'])

        if product.quantity >= 0:
            product.save()
            serializer.save()


class BasketByIdAPIView(generics.ListAPIView):
    serializer_class = fs.BasketSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Basket.objects.filter(user_id=user_id)


class AddOrderAPIView(generics.CreateAPIView):
    serializer_class = fs.OrderSerializer

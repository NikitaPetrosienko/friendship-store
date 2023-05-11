from rest_framework import generics

from .models import Product, Category, Brand
from .serializers import *


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductByIdAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['id']
        return Product.objects.filter(id=product_id)


class ProductByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)


class ProductByBrandAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        brand = self.kwargs['brand']
        return Product.objects.filter(brand=brand)


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class AddToBasketAPIView(generics.CreateAPIView):
    serializer_class = BasketSerializer


class BasketByIdAPIView(generics.ListAPIView):
    serializer_class = BasketSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Basket.objects.filter(user_id=user_id)


class AddOrderAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer

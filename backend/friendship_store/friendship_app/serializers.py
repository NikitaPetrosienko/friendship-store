from rest_framework import serializers
from .models import Product, Category, Brand


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

        #     (
        #     'product_name',
        #     'model',
        #     'price',
        #     'availability',
        #     'category',
        #     'brand',
        #     'description',
        #     'quantity',
        # )
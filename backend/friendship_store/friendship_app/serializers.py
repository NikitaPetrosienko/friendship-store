from rest_framework import serializers
from friendship_app.models import Product, Category, Brand, Basket, Order

from djoser.serializers import UserCreateSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(
            username=validated_data.get('email'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.save()
        return user


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


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

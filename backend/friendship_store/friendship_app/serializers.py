from rest_framework import serializers
import friendship_app.models as model
from django.contrib.auth.models import User

from djoser.serializers import UserCreateSerializer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Review
        fields = '__all__'


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'password')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')

        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с такой почтой уже существует!')

        user = self.Meta.model.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        user.save()

        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Brand
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = model.Basket
        fields = ('quantity', 'user_id', 'product_id')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Album
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Album
        fields = ('image',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Order
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.News
        fields = '__all__'

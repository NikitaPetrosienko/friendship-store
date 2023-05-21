from rest_framework import serializers
import friendship_app.models as model

from djoser.serializers import UserCreateSerializer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Review
        fields = '__all__'


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
    class Meta:
        model = model.Basket
        fields = '__all__'


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

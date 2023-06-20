from rest_framework import serializers
import friendship_app.models as model
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer


class ReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отзыва.
    """

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Review
        fields = '__all__'


class CustomUserCreateSerializer(UserCreateSerializer):
    """
    Сериализатор для создания пользователей с настраиваемым полем.
    """

    class Meta(UserCreateSerializer.Meta):
        """
        Мета-класс, наследуемый от Meta базового сериализатора UserCreateSerializer.
        """

        fields = ('email', 'password')

    def create(self, validated_data):
        """
        Создает нового пользователя с указанными данными.
        """

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


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.
    """

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Brand.
    """

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """

        model = model.Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.
    """

    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Product
        fields = (
            'id',
            'product_name',
            'model',
            'price',
            'availability',
            'category',
            'brand',
            'description',
            'quantity',
            'main_image',
            'size',
        )


class BasketPostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания объектов Basket.
    """

    token = serializers.CharField(required=False)

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Basket
        fields = ('token', 'product_id')


class BasketGetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения объектов Basket.
    """

    product_id = ProductSerializer()
    total = serializers.SerializerMethodField()

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Basket
        fields = ('id', 'quantity', 'product_id', 'total')

    def get_total(self, obj):
        """
        Метод для вычисления общей стоимости.
        """

        return obj.quantity * obj.product_id.price


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Сериализатор для объектов Favorite.
    """

    token = serializers.CharField(required=False)

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Favorite
        fields = ('token', 'product_id',)


class FavoriteGetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения объектов Favorite.
    """

    product_id = ProductSerializer()

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Favorite
        fields = ('id', 'user_id', 'product_id')


class AlbumSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Album.
    """

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Album
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор для поля image модели Album.
    """

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Album
        fields = ('image',)


class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Order.
    """

    token = serializers.CharField(required=False)

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.Order
        exclude = ('user_id', 'total_price',)


class NewsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели News.
    """

    class Meta:
        """
        Класс, содержащий информацию о модели, с которой будет работать сериализатор
        """
        model = model.News
        fields = '__all__'

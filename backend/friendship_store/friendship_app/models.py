from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Basket(models.Model):
    """
    Модель корзины.
    """
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        """
        Возвращает строковое представление объекта корзины.
        """
        return f'{self.user_id} - {self.product_id}'


class Favorite(models.Model):
    """
    Модель "Избранное" представляет отношение между пользователем и продуктом.
    """
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    """
    Поле ForeignKey, которое связывает модель Favorite с моделью User.
    on_delete=models.PROTECT означает, что при удалении пользователя избранный продукт будет сохранен.
    """
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    """
    Поле ForeignKey, которое связывает модель Favorite с моделью Product.
    on_delete=models.PROTECT означает, что при удалении продукта избранный продукт будет сохранен.
    """

    def __str__(self):
        """
        Метод __str__ возвращает строковое представление объекта Favorite.
        """
        return f'{self.user_id} - {self.product_id}'


class Order(models.Model):
    """
    Модель "Заказ" представляет информацию о заказе пользователя.
    """
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, default=0)
    """
    Поле ForeignKey, которое связывает модель Order с моделью User.
    on_delete=models.PROTECT означает, что при удалении пользователя заказ будет сохранен.
    По умолчанию равно 0.
    """
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=5, blank=True, null=True)
    apartment = models.CharField(max_length=5, blank=True, null=True)
    is_card_payment = models.BooleanField(default=False, blank=True, null=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        """
        Метод __str__ возвращает строковое представление объекта Order.
        """
        return f'Address: {self.district} {self.street} {self.house} {self.apartment}'


class Product(models.Model):
    """
    Класс, описывающий продукт.
    """
    product_name = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    main_image = models.URLField(default='http://example.com', blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта Product.
        """
        return f'{self.product_name} {self.model}'


class Category(models.Model):
    """
    Класс, описывающий категорию.
    """
    category_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта Category.
        """
        return self.category_name


class Brand(models.Model):
    """
    Класс, описывающий бренд.
    """
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    image = models.URLField(default='http://example.com', blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта Category.
        """
        return self.brand_name


class Image(models.Model):
    """
    Класс, описывающий изображение.
    """
    image = models.URLField(blank=True, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)


class Album(models.Model):
    """
    Класс, описывающий альбом.
    """
    image = models.URLField(blank=True, null=True)


class News(models.Model):
    """
    Класс, описывающий новости.
    """
    title = models.CharField(blank=True, null=True)
    main_image = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта News.
        """
        return self.title


class Review(models.Model):
    """
    Класс, описывающий ревью.
    """
    name_user = models.CharField(max_length=50, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта News.
        """
        return f'{self.name_user} {self.product_id}'

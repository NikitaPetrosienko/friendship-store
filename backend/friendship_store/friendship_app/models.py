from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_id} - {self.product_id}'


class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user_id} - {self.product_id}'


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=5)
    apartment = models.CharField(max_length=5, blank=True)
    is_card_payment = models.BooleanField(default=False)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Address: {self.district} {self.street} {self.house} {self.apartment}'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    model = models.CharField(max_length=50, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, blank=True, null=True)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    main_image = models.URLField(default='http://example.com')
    size = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product_name} {self.model}'



from django.db import models
from django.contrib.auth.models import User


class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user_id} - {self.product_id}'


class Order(models.Model):
    basket_id = models.ForeignKey('Basket', on_delete=models.PROTECT)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=5)
    apartment = models.CharField(max_length=5, blank=True)
    is_card_payment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Address: {self.district} {self.street} {self.house} {self.apartment}'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    model = models.CharField(max_length=50, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, blank=True)
    description = models.TextField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product_name} {self.model}'


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class Image(models.Model):
    image = models.ImageField()
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)

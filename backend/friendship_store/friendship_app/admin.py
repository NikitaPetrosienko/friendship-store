from django.contrib import admin

from .models import Product, Customer, Order, Category, Brand, Image

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Order)

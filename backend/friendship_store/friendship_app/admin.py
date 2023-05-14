from django.contrib import admin

from friendship_app.models import Product, Order, Category, Brand, Image, Basket, Album

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Basket)
admin.site.register(Album)

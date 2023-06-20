"""
В следующем коде регистрируются модели из Friendship App в административном интерфейсе Django.

Модуль admin импортируется из django.contrib.
Модели из модуля friendship_app.models импортируются и присваиваются переменной model.
Функция register вызывается для каждой модели на объекте admin.site для их регистрации в административном интерфейсе.
Зарегистрированные модели:

    Product
    Category
    Brand
    Image
    Order
    Basket
    Album
    News
    Review
    Favorite

Теперь эти модели будут доступны и управляемы через административный интерфейс Django.
"""

from django.contrib import admin
import friendship_app.models as model

admin.site.register(model.Product)
admin.site.register(model.Category)
admin.site.register(model.Brand)
admin.site.register(model.Image)
admin.site.register(model.Order)
admin.site.register(model.Basket)
admin.site.register(model.Album)
admin.site.register(model.News)
admin.site.register(model.Review)
admin.site.register(model.Favorite)

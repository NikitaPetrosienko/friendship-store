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

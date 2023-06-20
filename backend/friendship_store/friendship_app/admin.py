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


# admin.site.register(model.Product)
@admin.register(model.Product)
class ProductAdmin(admin.ModelAdmin):
    # inlines = [
    #     OrderInline,
    #     ProductInline,
    # ]
    list_display = 'pk', 'product_name', 'model', 'price', 'availability', 'category', 'brand', 'description_short', 'quantity', 'size'
    list_display_links = 'pk', 'product_name'
    ordering = ('pk', 'product_name',)
    search_fields = 'product_name', 'description',
    list_filter = ['availability']
    fieldsets = [
        ('Main' or None, {
            'fields': (
                'product_name', 'model', 'category', 'brand', 'description', 'quantity', 'size'),
        }),
        ('Price Options', {
            'fields': ('price',),
            'classes': ('wide', 'collapse'),
        }),
        ('Extra Options', {
            'fields': ('availability',),
            'classes': ('collapse',),
            'description': 'Field "archived" is for soft delete',
        }),
        # ('Date', {
        #     'fields': ('created_at',),
        #     'classes': ('wide',),
        # }),
        ('Images', {
            'fields': ('main_image',),
        }),
    ]

    def description_short(self, obj: model.Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'


# admin.site.register(model.Order)
@admin.register(model.Order)
class OrderAdmin(admin.ModelAdmin):
    # inlines = [
    #     ProductInline,
    # ]
    readonly_fields = 'created_at',
    list_display = ('pk', 'first_name', 'last_name', 'email', 'phoneNumber', 'district', 'street', 'house', 'apartment',
                    'is_card_payment', 'total_price', 'user_verbose', 'created_at')
    list_display_links = ('pk', 'first_name', 'email',)
    ordering = ('pk',)
    search_fields = ('pk', 'first_name', 'last_name', 'created_at', 'email', 'phoneNumber',)
    fieldsets = [
        ('Main', {
            'fields': ('first_name', 'last_name', 'email', 'phoneNumber', 'district', 'street', 'house', 'apartment',
                       'is_card_payment', 'total_price',),
            'classes': ('wide', 'collapse',)
        }),
        ('User Options', {
            'fields': ('user_id',),
            'classes': ('wide', 'collapse'),
        }),
        ('Date', {
            'fields': ('created_at',),
            'classes': ('wide',),
        }),
    ]

    def get_queryset(self, request):
        return model.Order.objects.select_related('user_id')

    def user_verbose(self, obj: model.Order) -> str:
        return obj.user_id.first_name or obj.user_id.username


@admin.register(model.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'category_name',
    list_display_links = 'category_name',
    ordering = 'category_name',
    search_fields = 'category_name',
    fieldsets = [
        ('Main', {
            'fields': ('category_name',),
            'classes': ('wide', 'collapse',)
        }),
    ]


# admin.site.register(model.Brand)
@admin.register(model.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name'),
    list_display_links = 'brand_name',
    ordering = 'brand_name',
    search_fields = 'brand_name',
    fieldsets = [
        ('Main', {
            'fields': ('brand_name',),
            'classes': ('wide', 'collapse',)
        }),
        ('Images', {
            'fields': ('image',),
        }),
    ]


# admin.site.register(model.Image)
@admin.register(model.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = 'product_id',
    list_display_links = 'product_id',
    ordering = 'product_id',
    search_fields = 'product_id',
    fieldsets = [
        ('Main', {
            'fields': ('product_id',),
            'classes': ('wide', 'collapse',)
        }),
        ('Images', {
            'fields': ('image',),
        }),
    ]


@admin.register(model.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = 'image',
    list_display_links = 'image',
    ordering = 'image',
    search_fields = 'image',
    fieldsets = [
        ('Images', {
            'fields': ('image',),
        }),
    ]


@admin.register(model.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = 'title', 'main_image', 'date', 'body',
    list_display_links = 'title',
    ordering = 'title', 'date', 'body',
    search_fields = 'title', 'date', 'body',
    fieldsets = [
        ('Main', {
            'fields': ('title', 'date', 'body',),
            'classes': ('wide', 'collapse',)
        }),
        ('Images', {
            'fields': ('main_image',),
        }),
    ]


# admin.site.register(model.Review)
@admin.register(model.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = 'name_user', 'body', 'product_id', 'created_at',
    list_display_links = 'name_user',
    ordering = 'name_user', 'body', 'product_id', 'created_at',
    search_fields = 'name_user', 'body', 'product_id', 'created_at',
    fieldsets = [
        ('Main', {
            'fields': ('name_user', 'body', 'product_id', 'created_at',),
            'classes': ('wide', 'collapse',)
        }),
    ]


# admin.site.register(model.Favorite)
@admin.register(model.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = 'user_id', 'product_id',
    list_display_links = 'user_id', 'product_id',
    ordering = 'user_id', 'product_id',
    search_fields = 'user_id', 'product_id',
    fieldsets = [
        ('Main', {
            'fields': ('user_id', 'product_id',),
            'classes': ('wide', 'collapse',)
        }),
    ]


@admin.register(model.Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = 'user_id', 'product_id', 'quantity', 'ordered',
    list_display_links = 'user_id', 'product_id', 'quantity', 'ordered',
    ordering = 'user_id', 'product_id', 'quantity', 'ordered',
    search_fields = 'user_id', 'product_id', 'quantity', 'ordered',
    fieldsets = [
        ('Main', {
            'fields': ('user_id', 'product_id', 'quantity', 'ordered',),
            'classes': ('wide', 'collapse',)
        }),
    ]

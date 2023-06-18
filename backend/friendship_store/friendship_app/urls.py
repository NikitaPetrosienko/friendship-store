"""
В представленном коде определены URL-шаблоны для конечных точек API в проекте Friendship Store с использованием функции
path из Django.

    Модуль path импортируется из django.urls.
    Импортируется модуль views из приложения Friendship App и присваивается переменной views.
    Шаблоны URL определены в виде списка и присвоены переменной urlpatterns.
    Каждый шаблон URL создается с использованием функции path и связывает определенный URL с соответствующим
    представлением.
    Представления, используемые для каждого шаблона URL, импортируются из модуля views.
    Некоторые шаблоны URL включают дополнительные параметры, захватываемые из URL с использованием угловых скобок (< >).
    Список urlpatterns расширяется путем добавления шаблонов URL, определенных в переменной doc_urls из модуля
    friendship_app.yasg.
"""

from django.urls import path
import friendship_app.views as views
from friendship_app.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('products/', views.ProductAPIView.as_view()),
    path('brands/', views.BrandAPIView.as_view()),
    path('categories/', views.CategoryAPIView.as_view()),
    path('order/', views.OrderAPIView.as_view()),
    path('basket/', views.AddToBasketAPIView.as_view()),
    path('albums/', views.AlbumAPIView.as_view()),
    path('news/', views.NewsAPIView.as_view()),
    path('review/', views.CreateReviewAPIView.as_view()),
    path('favorites/', views.FavoriteCreateAPIView.as_view()),
    path('delete_favorite/<int:pk>/', views.FavoriteDestroyAPIView.as_view()),
    path('favorites/<str:token>/', views.FavoriteListAPIView.as_view()),
    path('product/<str:product>/', views.ProductByIdAPIView.as_view()),
    path('product_by_category/<str:category>/', views.ProductByCategoryAPIView.as_view()),
    path('product_by_brand/<str:brand>/', views.ProductByBrandAPIView.as_view()),
    path('basket/<int:basket_id>/<str:incr>/', views.BasketQuantityAPIView.as_view()),
    path('basket/<str:token>/', views.BasketGetAPIView.as_view()),
    path('search/<str:word>/', views.SearchAPIView.as_view())
]

urlpatterns += doc_urls

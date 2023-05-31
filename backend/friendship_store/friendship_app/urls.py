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

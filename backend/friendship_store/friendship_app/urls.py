from django.urls import path, include
import friendship_app.views as views
from friendship_app.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('products/', views.ProductAPIView.as_view()),
    path('brands/', views.BrandAPIView.as_view()),
    path('categories/', views.CategoryAPIView.as_view()),
    path('order/', views.NewOrderAPIView.as_view()),
    path('basket/', views.AddToBasketAPIView.as_view()),
    path('albums/', views.AlbumAPIView.as_view()),
    path('image/<int:product_id>', views.ImageAPIView.as_view()),
    path('product_by_id/<int:product_id>/', views.ProductByIdAPIView.as_view()),
    path('product_by_category/<int:category_id>/', views.ProductByCategoryAPIView.as_view()),
    path('product_by_brand/<int:brand_id>/', views.ProductByBrandAPIView.as_view()),
    path('basket/<int:user_id>/', views.BasketByIdAPIView.as_view()),
]

urlpatterns += doc_urls
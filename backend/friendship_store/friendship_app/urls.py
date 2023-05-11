from django.urls import path
from .views import *
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('brands/', BrandAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('order', AddOrderAPIView.as_view()),
    path('basket', AddToBasketAPIView.as_view()),
    path('product_by_id/<int:id>', ProductByIdAPIView.as_view()),
    path('product_by_category/<int:category>', ProductByCategoryAPIView.as_view()),
    path('product_by_brand/<int:brand>', ProductByBrandAPIView.as_view()),
    path('basket/<int:user_id>', BasketByIdAPIView.as_view()),
]

urlpatterns += doc_urls

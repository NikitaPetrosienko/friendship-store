from django.urls import path

from .views import *

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('product_by_id/<str:id>', ProductByIdAPIView.as_view()),
    path('product_by_category/<str:category>', ProductByCategoryAPIView.as_view()),
    path('product_by_brand/<str:brand>', ProductByBrandAPIView.as_view()),
    path('brands/', BrandAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
]
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers

# from .views import CategoryListMVS, ProductListMVS

# router = routers.DefaultRouter()
# router.register('category', CategoryListMVS)
# router.register('product', ProductListMVS)
# urlpatterns = [
#     path('', include(router.urls))
# ]

from django.contrib import admin
from django.urls import path, include

from .views import ProductListAPIView, BrandListAPIView
from .views import FirmListAPIView, PurchasesListAPIView, SalesListAPIView
from .views import CategoryListAPIView, CategoryProductListAPIView, CategoryCreateAPIView

urlpatterns = [
    # Urls for GET method
    path('categoryList/', CategoryListAPIView.as_view()),
    path('categoryList/<str:name>/', CategoryProductListAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
    path('brand/', BrandListAPIView.as_view()),
    path('firm/', FirmListAPIView.as_view()),
    path('purchases/', PurchasesListAPIView.as_view()),
    path('sales/', SalesListAPIView.as_view()),

    # Urls for POST method
    path('categoryCreate/', CategoryCreateAPIView.as_view()),
]
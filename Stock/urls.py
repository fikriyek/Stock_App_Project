from django.contrib import admin
from django.urls import path, include

from .views import CategoryListAPIView, CategoryProductListAPIView, CategoryCreateAPIView
from .views import BrandListAPIView, BrandCreateAPIView
from .views import FirmListAPIView, FirmCreateAPIView
from .views import ProductListAPIView, ProductCreateAPIView
from .views import PurchasesListAPIView, PurchasesCreateAPIView
from .views import SalesListAPIView, SalesCreateAPIView

urlpatterns = [
    # Urls for GET method
    path('categoryList/', CategoryListAPIView.as_view()),
    path('categoryList/<str:name>/', CategoryProductListAPIView.as_view()),
    path('brandList/', BrandListAPIView.as_view()),
    path('productList/', ProductListAPIView.as_view()),
    path('firmList/', FirmListAPIView.as_view()),
    path('purchasesList/', PurchasesListAPIView.as_view()),
    path('salesList/', SalesListAPIView.as_view()),

    # Urls for POST method
    path('categoryCreate/', CategoryCreateAPIView.as_view()),
    path('brandCreate/', BrandCreateAPIView.as_view()),
    path('productCreate/', ProductCreateAPIView.as_view()),
    path('firmCreate/', FirmCreateAPIView.as_view()),
    path('purchasesCreate/', PurchasesCreateAPIView.as_view()),  # TO DO
    path('salesCreate/', SalesCreateAPIView.as_view()),  # TO DO
]
from django.contrib import admin
from django.urls import path, include

from .views import CategoryListAPIView, CategoryProductListAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView
from .views import BrandListAPIView, BrandCreateAPIView, BrandUpdateAPIView, BrandDeleteAPIView
from .views import FirmListAPIView, FirmCreateAPIView, FirmUpdateAPIView, FirmDeleteAPIView
from .views import ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView
from .views import PurchasesListAPIView, PurchasesCreateAPIView, PurchasesUpdateAPIView, PurchasesDeleteAPIView
from .views import SalesListAPIView, SalesCreateAPIView, SalesUpdateAPIView, SalesDeleteAPIView

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
    path('categoryCreate/', CategoryCreateAPIView.as_view()),  # TO BE TESTED
    path('brandCreate/', BrandCreateAPIView.as_view()),  # TO BE TESTED
    path('productCreate/', ProductCreateAPIView.as_view()),
    path('firmCreate/', FirmCreateAPIView.as_view()),  # TO BE TESTED
    path('purchasesCreate/<int:product_id>/', PurchasesCreateAPIView.as_view()),
    path('salesCreate/', SalesCreateAPIView.as_view()),  # TO DO

    # Urls for UPDATE method
    path('categoryUpdate/<int:pk>/', CategoryUpdateAPIView.as_view()),  # TO BE TESTED
    path('brandUpdate/<int:pk>/', BrandUpdateAPIView.as_view()),  # TO BE TESTED
    path('productUpdate/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('firmUpdate/<int:pk>/', FirmUpdateAPIView.as_view()),  # TO BE TESTED
    path('purchasesUpdate/<int:pk>/', PurchasesUpdateAPIView.as_view()),
    path('salesUpdate/<int:pk>/', SalesUpdateAPIView.as_view()),  # TO BE TESTED

    # Urls for DELETE method
    path('categoryDelete/<int:pk>/', CategoryDeleteAPIView.as_view()),  # TO BE TESTED
    path('brandDelete/<int:pk>/', BrandDeleteAPIView.as_view()),  # TO BE TESTED
    path('productDelete/<int:pk>/', ProductDeleteAPIView.as_view()),  # TO BE TESTED
    path('firmDelete/<int:pk>/', FirmDeleteAPIView.as_view()),  # TO BE TESTED
    path('purchasesDelete/<int:pk>/', PurchasesDeleteAPIView.as_view()),
    path('salesDelete/<int:pk>/', SalesDeleteAPIView.as_view()),  # TO BE TESTED
]
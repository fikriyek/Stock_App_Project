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

from .views import CategoryListCreateAPIView, CategoryProductAPIView, ProductListAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<str:name>/', CategoryProductAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
]
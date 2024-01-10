from django.contrib import admin
from django.urls import path, include

from .views import CategoryListCreateAPIView, CategoryProductAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<str:name>/', CategoryProductAPIView.as_view()),
]
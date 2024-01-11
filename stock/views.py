from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Brand, Product
from .serializers import CategorySerializer, CategoryDetailSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['name']
    search_fields = ['name']

class CategoryProductAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    def get_queryset(self):
        category_name = self.kwargs['name']
        categories = Category.objects.filter(name = category_name)
       # product = Product.objects.filter(name = category_name)

        return categories
    
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
from django.shortcuts import render

from .models import Category, Brand, Product
from .serializers import CategorySerializer, CategoryDetailSerializer

from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryProductAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    # def get_queryset(self):
    #     category_name = self.kwargs['name']
    #     categories = Category.objects.filter(name__iexact=category_name)

    #     return categories.products

    #     # for category in categories:
    #     #     product = Product.objects.filter(category=category)            
    #     #     return product

     
    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Category Table
class Category(models.Model):
    name = models.CharField(max_length=30, unique = True)

    def __str__(self):
        return self.name
    
# Brand Table
class Brand(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True, upload_to='Brand')

    def __str__(self):
        return self.name
    
# Product Table
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.PositiveSmallIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Firm Table
class Firm(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True, unique=True)
    phone = models.PositiveSmallIntegerField(null=True)
    address = models.TextField(max_length=120, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='Firm')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

# Purchases Table
class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(null=True)
    price = models.PositiveSmallIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}"
    
# Sales Table
class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(null=True)
    price = models.PositiveSmallIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}"
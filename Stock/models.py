from django.db import models

# Create your models here.

# Category Table
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
# Brand Table
class Brand(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(blank=True, null=True, upload_to='Brand')

    def __str__(self):
        return self.name
    
# Product Table
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.PositiveSmallIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name - self.category - self.brand - self.stock - self.created - 
                  self.updated}"

# Firm Table
class Firm(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    phone = models.PositiveSmallIntegerField(null=True)
    address = models.TextField(max_length=120, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='Firm')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name - self.created - self.updated}"

# Purchases Table
class Purchases(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(null=True)
    price = models.PositiveSmallIntegerField(null=True)
    price_total = models.PositiveBigIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firm - self.brand - self.product - self.quantity - self.price - 
                  self.price_total- self.created - self.updated}"
    
# Sales Table
class Sales(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(null=True)
    price = models.PositiveSmallIntegerField(null=True)
    price_total = models.PositiveBigIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product - self.brand - self.quantity - self.price - self.price_total - 
                  self.created - self.updated}"


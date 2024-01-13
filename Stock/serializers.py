from rest_framework import serializers

from .models import Category, Brand, Product, Firm, Purchases, Sales

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'brand',
            'brand_id',
            'stock',
            'created',
            'updated',
        )

        read_only_fields = ('stock',)

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):

    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'product_count',
        )
    
    def get_product_count(self, obj):
        return obj.product_set.count()

# Category Detail Serializer
class CategoryDetailSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'product',
        )
        read_only_fields = (
            'id',
            'product',
        )

# class CategoryDetailSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     class Meta:
#         model = Category
#         fields = (
#             'id',
#             'name',
#             'category',
#         )   

# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image',
        )

# Firm Serializer
class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'address',
            'image',
        )

# Purchases Serializer
class PurchasesSerializer(serializers.ModelSerializer):
    
    price_total = serializers.SerializerMethodField()

    user_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    firm_id = serializers.IntegerField()
    firm = serializers.StringRelatedField()

    brand_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()

    product_id = serializers.IntegerField()
    product = serializers.StringRelatedField()

    class Meta:
        model = Purchases
        fields = (
            'user_id',
            'user',
            'firm_id',
            'firm',
            'brand_id',
            'brand',
            'product_id',
            'product',
            'quantity',
            'price',
            'price_total',

        )

    def get_price_total(self, obj):
        self.price_total = obj.price * obj.quantity
        return self.price_total

# Sales Serializer
class SalesSerializer(serializers.ModelSerializer):

    price_total = serializers.SerializerMethodField()

    user_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    product_id = serializers.IntegerField()
    product = serializers.StringRelatedField()

    brand_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()

    class Meta:
        model = Sales
        fields = (
            'user_id',
            'user',
            'brand_id',
            'brand',
            'product_id',
            'product',
            'quantity',
            'price',
            'price_total',
        )

    def get_price_total(self, obj):
        self.price_total = obj.price * obj.quantity
        return self.price_total 
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
            'name',
            'id',
            'category',
            'category_id',
            'brand',
            'brand_id',
            'stock',
            'created',
            'updated',
        )


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
            'name',
            'image',
        )
    
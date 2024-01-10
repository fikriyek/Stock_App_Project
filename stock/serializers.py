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
            'category_id',
            'category',
            'brand_id',
            'brand',
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

    product_count = serializers.SerializerMethodField()

    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'product_count',
            'product',
        )
        read_only_fields = (
            'id',
            'product',
        )


    def get_product_count(self, obj):
        return obj.product_set.count()
    
    # def create(self, validated_data):
    #     product_data = validated_data.pop('product')

    #     category = Category.objects.create(**validated_data)


    #     for product in product_data:
    #         prod = Product.objects.create(**product)
    #         category.product.add(prod)

    #     category.save()
    #     return category



# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = (
            'name',
            'image',
        )
    
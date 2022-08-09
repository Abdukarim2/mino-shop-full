from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'get_img_url']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'slug',
            'price',
            'priceDolor',
            'about',
            'get_sizes',
            'get_colors',
            'material',
            'get_img_url'
        ]

from .serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product


class CategoryList(APIView):
    """List category"""
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductByCategory(APIView):
    """Product list by category api"""
    def get(self, request, category_id, format=None):
        product = None
        if request.query_params.get('limit'):
            try:
                limit = int(request.query_params.get('limit'))
                product = Product.objects.select_related('category')\
                    .prefetch_related("color", "size", "material").filter(category=category_id)\
                    .order_by("?")[0:limit]
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product = Product.objects.select_related('category') \
                    .prefetch_related("color", "size", "material").filter(category=category_id).order_by("?")
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class ProductList(APIView):
    """Products list api"""
    def get(self, request, format=None):
        if request.query_params.get('limit'):
            limit = int(request.query_params.get('limit'))
            try:
                if request.query_params.get('random'):
                    product = Product.objects.select_related('category') \
                        .prefetch_related("color", "size", "material") \
                        .all().order_by("?")[0:limit]
                else:
                    product = Product.objects.select_related('category') \
                        .prefetch_related("color", "size", "material") \
                        .all()[0:limit]
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            product = Product.objects.select_related('category').prefetch_related("color", "size", "material").all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    """Product detail api"""
    def get(self, request, id, format=None):
        try:
            product = Product.objects.select_related('category').prefetch_related("color", "size", "material").get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

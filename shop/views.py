from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category
from shop.serializers import CategorySerializer

from shop.models import Product
from shop.serializers import ProductSerializer


class CategoryAPIView(APIView):

    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

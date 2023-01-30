from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category
from shop.serializers import CategorySerializer


class CategoryAPIView(APIView):

    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
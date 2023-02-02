from rest_framework.serializers import ModelSerializer

from shop.models import Category
from shop.models import Product
from shop.models import Article


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','date_created','name']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','date_created','name','category']

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','date_created','name','price','product']

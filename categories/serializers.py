from rest_framework import serializers

from .models import Categories, Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = 'name', 'description'


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())
    class Meta:
        model = Product
        fields = 'title', 'relevant', 'description', 'category'

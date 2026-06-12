from rest_framework import serializers

from apps.products.models import Product


class ProductUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

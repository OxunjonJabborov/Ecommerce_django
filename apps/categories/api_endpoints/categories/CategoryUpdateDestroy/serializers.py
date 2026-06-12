from rest_framework import serializers

from apps.categories.models import Category


class CatgoryUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

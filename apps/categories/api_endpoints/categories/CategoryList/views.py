from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.categories.api_endpoints.categories.CategoryList.serializers import CategoryListSerializer
from apps.categories.models import Category


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

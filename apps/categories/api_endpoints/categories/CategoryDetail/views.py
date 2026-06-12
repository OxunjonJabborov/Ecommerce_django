from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.categories.api_endpoints.categories.CategoryDetail.serializers import CategoryDetailSerializer
from apps.categories.models import Category


@api_view(['GET'])
def category_detail_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Kategoriya topilmadi...'}, status=404)

    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.categories.api_endpoints.categories.CategoryUpdateDestroy.serializers import CatgoryUpdateDestroySerializer
from apps.categories.models import Category


@api_view(['PATCH', 'DELETE'])
def category_update_or_delete_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Kategoriya topilmadi...'}, status=404)

    if request.method == 'PATCH':
        serializer = CatgoryUpdateDestroySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            category = serializer.save()
            return Response(CatgoryUpdateDestroySerializer(category).data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        category.delete()
        return Response(status=204)

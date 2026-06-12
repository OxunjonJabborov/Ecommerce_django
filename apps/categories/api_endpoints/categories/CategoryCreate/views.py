from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.categories.api_endpoints.categories.CategoryCreate.serializers import CategoryCreateSerializer

@api_view(['POST'])
def create_category_view(request):
    serializer = CategoryCreateSerializer(data=request.data)
    if serializer.is_valid():
        category = serializer.save()
        return Response(CategoryCreateSerializer(category).data, status=201)
    return Response(serializer.errors, status=400)
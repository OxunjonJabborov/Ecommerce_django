from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.ProductCreate.serializers import ProductCreateSerializer


@api_view(['POST'])
def create_product_view(request):
    serializer = ProductCreateSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save()
        return Response(ProductCreateSerializer(product).data, status=201)
    return Response(serializer.errors, status=400)

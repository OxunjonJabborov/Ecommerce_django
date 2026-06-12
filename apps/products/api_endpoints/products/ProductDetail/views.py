from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.ProductDetail.serializers import ProductDetailSerializer
from apps.products.models import Product


@api_view(['GET'])
def product_detail_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Mahsulot topilmadi...'}, status=404)

    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)
    
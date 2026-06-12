from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.ProductUpdateDestroy.serializers import ProductUpdateDestroySerializer
from apps.products.models import Product


@api_view(['PATCH', 'DELETE'])
def product_update_or_delete_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Mahsulot topilmadi...'}, status=404)

    if request.method == 'PATCH':
        serializer = ProductUpdateDestroySerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductUpdateDestroySerializer(product).data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)
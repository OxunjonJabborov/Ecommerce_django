from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.api_endpoints.orders.OrderCreate.serializer import OrderCreateSerializer


@api_view(['POST'])
def create_order_view(request):
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        return Response(OrderCreateSerializer(order).data, status=201)
    return Response(serializer.errors, status=400)

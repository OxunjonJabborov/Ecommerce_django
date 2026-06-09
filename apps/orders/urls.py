from django.urls import path

from apps.orders.views import order_list_view, order_detail_view
from apps.orders.api_endpoints.orders.OrderList.views import order_list


urlpatterns = [
    path('', order_list_view, name='order_list'),
    path('<int:order_id>/', order_detail_view, name='order_detail'),
    path('api/', order_list, name='order_list')
]
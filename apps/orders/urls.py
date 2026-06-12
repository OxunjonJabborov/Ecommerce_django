from django.urls import path

from apps.orders.views import order_list_view, order_detail_view
from apps.orders.api_endpoints.orders.OrderList.views import order_list_view
from apps.orders.api_endpoints.orders.OrderCreate.views import create_order_view
from apps.orders.api_endpoints.orders.OrderDetail.views import order_detail_view
from apps.orders.api_endpoints.orders.OrderUpdateDestroy.views import order_update_or_delete_view


urlpatterns = [
    path('', order_list_view, name='orders_list'),
    # path('<int:order_id>/', order_detail_view, name='order_detail'),
    path('list/', order_list_view, name='order_list'),
    path('create/', create_order_view, name='create_order'),
    path('<int:pk>/', order_detail_view, name='order_detail'),
    path('update/<int:pk>/', order_update_or_delete_view, name='order_update_or_delete'),
]
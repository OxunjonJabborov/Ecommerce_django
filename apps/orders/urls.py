from django.urls import path

from apps.orders.views import order_list_view, order_detail_view


urlpatterns = [
    path('my-orders/', order_list_view, name='order_list'),
    path('my-orders/<int:order_id>/', order_detail_view, name='order_detail'),
]
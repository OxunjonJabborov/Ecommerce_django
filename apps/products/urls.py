from django.urls import path

from apps.products.views import product_list_view, product_detail_view
from apps.products.api_endpoints.products.ProductList.views import product_list

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:product_id>/', product_detail_view, name='product_detail'),
    path('api/', product_list, name='product_list'),
]
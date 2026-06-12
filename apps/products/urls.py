from django.urls import path

from apps.products.views import product_list_view, product_detail_view
from apps.products.api_endpoints.products.ProductList.views import product_list_view
from apps.products.api_endpoints.products.ProductCreate.views import create_product_view
from apps.products.api_endpoints.products.ProductDetail.views import product_detail_view
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update_or_delete_view


urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('list/', product_list_view, name='product_list'),
    path('create/', create_product_view, name='product_create'),
    path('<int:pk>/', product_detail_view, name='product_detail'),
    path('update/<int:pk>/', product_update_or_delete_view, name='product_update_or_delete'),
]
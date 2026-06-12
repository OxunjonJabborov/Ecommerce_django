from django.urls import path

from apps.categories.views import categories_list_view
from apps.categories.api_endpoints.categories.CategoryList.views import category_list_view
from apps.categories.api_endpoints.categories.CategoryCreate.views import create_category_view
from apps.categories.api_endpoints.categories.CategoryDetail.views import category_detail_view
from apps.categories.api_endpoints.categories.CategoryUpdateDestroy.views import category_update_or_delete_view


urlpatterns = [
    path('', categories_list_view, name='categories_list'),
    path('list/', category_list_view, name='category_list'),
    path('create/', create_category_view, name='create_category'),
    path('<int:pk>/', category_detail_view, name='category_detail'),
    path('update/<int:pk>/', category_update_or_delete_view, name='update_or_delete_category'),
]
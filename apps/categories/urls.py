from django.urls import path

from apps.categories.views import categories_list_view
from apps.categories.api_endpoints.categories.CategoryList.views import category_list


urlpatterns = [
    path('api/', category_list, name='category_list'),
    path('', categories_list_view, name='categories_list'),
]
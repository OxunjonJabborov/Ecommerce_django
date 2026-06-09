from django.urls import path

from apps.categories.views import categories_list_view


urlpatterns = [
    path('', categories_list_view, name='category_list')
]
from django.urls import path

from apps.users.views import user_profile_view
from apps.users.api_endpoints.users.UserList.views import user_list_view
from apps.users.api_endpoints.users.UserCreate.views import create_user_view
from apps.users.api_endpoints.users.UserDetail.views import user_detail_view
from apps.users.api_endpoints.users.UserUpdateDestroy.views import user_update_or_delete_view


urlpatterns = [
    path('', user_profile_view, name='user_profile'),
    path('list/', user_list_view, name='user_list'),
    path('create/', create_user_view, name='create_user'),
    path('<int:pk>/', user_detail_view, name='user_detail'),
    path('update/<int:pk>/', user_update_or_delete_view, name='user_update_or_delete'),
]

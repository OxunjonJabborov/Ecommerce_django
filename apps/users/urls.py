from django.urls import path

from apps.users.views import user_profile_view
from apps.users.api_endpoints.users.UserList.views import user_list


urlpatterns = [
    path('', user_profile_view, name='user_profile'),
    path('api/', user_list, name='user_list'),
]

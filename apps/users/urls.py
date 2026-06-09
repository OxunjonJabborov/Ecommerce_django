from django.urls import path

from apps.users.views import user_profile_view


urlpatterns = [
    path('', user_profile_view, name='user_profile')
]

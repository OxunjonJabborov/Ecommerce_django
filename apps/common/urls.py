from django.urls import path

from apps.common import views


urlpatterns = [
    path('', views.home_view, name='home'),
]
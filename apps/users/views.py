from django.shortcuts import render, get_object_or_404

from apps.users.models import User

# Create your views here.


def user_profile_view(request):
    user_profile = get_object_or_404(User, id=1)
    return render(request, 'users/user_profile.html', {'user_profile': user_profile})
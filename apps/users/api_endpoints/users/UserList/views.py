from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.api_endpoints.users.UserList.serializers import UserListSerializer
from apps.users.models import User


@api_view(['GET'])
def user_list_view(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(serializer.data)

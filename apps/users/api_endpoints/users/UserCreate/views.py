from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.api_endpoints.users.UserCreate.serializers import UserCreateSerializer


@api_view(['POST'])
def create_user_view(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserCreateSerializer(user).data, status=201)
    return Response(serializer.errors, status=400)
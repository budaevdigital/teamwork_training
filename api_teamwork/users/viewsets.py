from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer
from users.services import UserViewSetService


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request):
        return UserViewSetService(request).execute_post()
    

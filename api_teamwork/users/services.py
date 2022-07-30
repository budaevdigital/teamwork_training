import json
import requests
from rest_framework import status
from rest_framework.response import Response
from users.models import CustomUser


from users.serializers import UserSerializer

class UserViewSetService:
    
    __slots__ = 'request',

    def __init__(self, request=None):
        self.request = request
        
    def execute_post(self):
        """
        Create new user and send code on the mail
        """
        if self.request is not None:
            user = CustomUser(email = self.request.data["email"], username = self.request.data["username"])
            if user is not None:
                # отправить код подтвержения на почту
                return Response(status=status.HTTP_200_OK) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
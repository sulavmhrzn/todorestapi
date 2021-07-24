from rest_framework import generics
from .serializers import UserRegisterSerializer
from django.contrib.auth.models import User


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects

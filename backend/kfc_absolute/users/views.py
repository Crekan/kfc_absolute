from rest_framework import generics
from rest_framework import permissions

from .models import User
from .serializers import CustomUserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

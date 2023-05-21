from rest_framework import generics, permissions

from .models import Vakantie
from .serializers import VakantieCreateSerializer, VakantieSerializer


class VakantieView(generics.ListAPIView):
    queryset = Vakantie.objects.all()
    serializer_class = VakantieSerializer
    permission_classes = (permissions.IsAuthenticated,)


class VakantieCreateView(generics.CreateAPIView):
    queryset = Vakantie.objects.all()
    serializer_class = VakantieCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

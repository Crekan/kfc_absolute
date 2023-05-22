from django.shortcuts import redirect
from rest_framework import generics, permissions

from .mixins import VakantieFilterMixin
from .serializers import VakantieCreateSerializer, VakantieSerializer


class VakantieView(VakantieFilterMixin, generics.ListAPIView):
    """
    Vacation viewing
    """

    serializer_class = VakantieSerializer
    permission_classes = (permissions.IsAuthenticated,)


class VakantieCreateView(VakantieFilterMixin, generics.CreateAPIView):
    """
    vacation addition
    """

    serializer_class = VakantieCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return redirect('/api/v1/vakantie/create/')

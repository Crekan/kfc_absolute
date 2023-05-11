from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics

from .models import Temporary
from .serializers import TemporaryCreateSerializer, TemporarySerializer


class TemporaryView(generics.ListAPIView):
    serializer_class = TemporarySerializer

    def get_queryset(self):
        return Temporary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TemporaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TemporaryCreateSerializer

    def get_queryset(self):
        return Temporary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TemporaryCreateView(generics.CreateAPIView):
    serializer_class = TemporaryCreateSerializer

    def get_queryset(self):
        return Temporary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = self.serializer_class.Meta.model.objects.get(id=response.data['id'])
        url = reverse('temporary_create')
        return HttpResponseRedirect(url)

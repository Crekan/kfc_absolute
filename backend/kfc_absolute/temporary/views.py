from datetime import datetime, timedelta

from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Temporary
from .serializers import TemporaryCreateSerializer, TemporarySerializer
from .tasks import delete_record


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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        delete_record.apply_async(args=(serializer.instance.id,), eta=datetime.now() + timedelta(days=7))

        return redirect('/api/v1/temporary/create/')

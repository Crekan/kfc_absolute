from datetime import datetime, timedelta

from django.shortcuts import redirect
from rest_framework import generics, permissions

from users.models import User
from users.serializers import CustomUserAdminSerializer

from .mixins import UserFilterMixin
from .serializers import TemporaryCreateSerializer, TemporarySerializer
from .tasks import delete_record


class AdminView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserAdminSerializer
    permission_classes = (permissions.IsAdminUser,)


class TemporaryView(UserFilterMixin, generics.ListAPIView):
    serializer_class = TemporarySerializer
    permission_classes = (permissions.IsAuthenticated,)


class TemporaryDetailView(UserFilterMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TemporaryCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TemporaryCreateView(UserFilterMixin, generics.CreateAPIView):
    serializer_class = TemporaryCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        delete_record.apply_async(args=(serializer.instance.id,), eta=datetime.now() + timedelta(days=7))

        return redirect('/api/v1/temporary/create/')

from django.shortcuts import redirect
from rest_framework import generics, permissions

from .mixins import AdjustmentWorkingHoursFilterMixin
from .models import ShiftManager
from .serializers import (AdjustmentWorkingHoursCreateSerializers,
                          AdjustmentWorkingHoursSerializers,
                          ShiftManagerCreateSerializer, ShiftManagerSerializer)


class ShiftManagerView(generics.ListAPIView):
    """
    Viewing managers
    """

    queryset = ShiftManager.objects.all()
    serializer_class = ShiftManagerSerializer
    permission_classes = (permissions.IsAdminUser,)


class ShiftManagerCreateView(generics.CreateAPIView):
    """
    Adding managers
    """

    queryset = ShiftManager.objects.all()
    serializer_class = ShiftManagerCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class AdjustmentWorkingHoursView(AdjustmentWorkingHoursFilterMixin, generics.ListAPIView):
    """
    Viewing time adjustments
    """

    serializer_class = AdjustmentWorkingHoursSerializers
    permission_classes = (permissions.IsAuthenticated,)


class AdjustmentWorkingHoursCreateView(AdjustmentWorkingHoursFilterMixin, generics.CreateAPIView):
    """
    Adding time adjustments
    """

    serializer_class = AdjustmentWorkingHoursCreateSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return redirect('/api/v1/adjustments_to_working_hours/create/')

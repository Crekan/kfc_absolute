from rest_framework import generics, permissions

from .models import AdjustmentWorkingHours, ShiftManager
from .serializers import (AdjustmentWorkingHoursCreateSerializers,
                          AdjustmentWorkingHoursSerializers,
                          ShiftManagerCreateSerializer, ShiftManagerSerializer)


class ShiftManagerView(generics.ListAPIView):
    queryset = ShiftManager.objects.all()
    serializer_class = ShiftManagerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ShiftManagerCreateView(generics.CreateAPIView):
    queryset = ShiftManager.objects.all()
    serializer_class = ShiftManagerCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AdjustmentWorkingHoursView(generics.ListAPIView):
    queryset = AdjustmentWorkingHours.objects.all()
    serializer_class = AdjustmentWorkingHoursSerializers
    permission_classes = (permissions.IsAuthenticated,)


class AdjustmentWorkingHoursCreateView(generics.CreateAPIView):
    queryset = AdjustmentWorkingHours.objects.all()
    serializer_class = AdjustmentWorkingHoursCreateSerializers
    permission_classes = (permissions.IsAuthenticated,)

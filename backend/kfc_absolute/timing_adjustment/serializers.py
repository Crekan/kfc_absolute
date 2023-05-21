from rest_framework import serializers

from .models import AdjustmentWorkingHours, ShiftManager


class ShiftManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftManager
        fields = ['id', 'full_name']


class ShiftManagerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftManager
        fields = ['full_name']


class AdjustmentWorkingHoursSerializers(serializers.ModelSerializer):
    manager = ShiftManagerSerializer()

    class Meta:
        model = AdjustmentWorkingHours
        fields = ['id', 'date', 'start_time', 'end_time', 'launch', 'manager']


class AdjustmentWorkingHoursCreateSerializers(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=ShiftManager.objects.all())

    class Meta:
        model = AdjustmentWorkingHours
        fields = ['date', 'start_time', 'end_time', 'launch', 'manager']

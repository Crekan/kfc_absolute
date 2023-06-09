from .models import AdjustmentWorkingHours


class AdjustmentWorkingHoursFilterMixin:
    def get_queryset(self):
        return AdjustmentWorkingHours.objects.filter(user=self.request.user).select_related('manager')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

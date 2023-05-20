from .models import Temporary


class UserFilterMixin:
    def get_queryset(self):
        return Temporary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

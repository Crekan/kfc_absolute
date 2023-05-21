from .models import Vakantie


class VakantieFilterMixin:
    def get_queryset(self):
        return Vakantie.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

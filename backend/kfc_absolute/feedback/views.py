from rest_framework import generics, permissions

from .models import Feedback
from .serializers import FeedbackCreateSerializer, FeedbackSerializer


class FeedbackView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

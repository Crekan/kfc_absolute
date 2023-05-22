from rest_framework import generics, permissions

from .models import Feedback
from .serializers import FeedbackCreateSerializer, FeedbackSerializer


class FeedbackView(generics.ListAPIView):
    """
    View vacation request
    """

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FeedbackCreateView(generics.CreateAPIView):
    """
    Creating a vacation request
    """

    queryset = Feedback.objects.all()
    serializer_class = FeedbackCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

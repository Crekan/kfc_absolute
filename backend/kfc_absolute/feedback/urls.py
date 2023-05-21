from django.urls import path

from .views import FeedbackCreateView, FeedbackView

urlpatterns = [
    path('feedback/', FeedbackView.as_view(), name='feedback_view'),
    path('feedback/create/', FeedbackCreateView.as_view(), name='feedback_create'),
]

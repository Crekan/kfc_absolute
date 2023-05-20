from django.urls import path

from temporary.views import TemporaryCreateView, TemporaryDetailView, TemporaryView, AdminView

urlpatterns = [
    path('temporary/', TemporaryView.as_view(), name='temporary'),
    path('temporary/<int:pk>/', TemporaryDetailView.as_view(), name='temporary_detail'),
    path('temporary/create/', TemporaryCreateView.as_view(), name='temporary_create'),
    path('temporary/view/', AdminView.as_view(), name='admin_view'),
]

from django.urls import path

from .views import VakantieCreateView, VakantieView

urlpatterns = [
    path('vakantie/', VakantieView.as_view(), name='vakantie_view'),
    path('vakantie/create/', VakantieCreateView.as_view(), name='vakantie_create'),
]

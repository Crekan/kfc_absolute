from django.urls import path

from .views import VakantieView, VakantieCreateView

urlpatterns = [
    path('vakantie/', VakantieView.as_view(), name='vakantie_view'),
    path('vakantie/create/', VakantieCreateView.as_view(), name='vakantie_create'),
]

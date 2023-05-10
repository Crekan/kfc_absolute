from django.urls import path, include

from users.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('', include('rest_framework.urls')),
]

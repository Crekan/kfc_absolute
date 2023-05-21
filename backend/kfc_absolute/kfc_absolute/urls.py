from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('users.urls')),
    path('api/v1/', include('temporary.urls')),
    path('api/v1/', include('feedback.urls')),
    path('api/v1/', include('vakantie.urls')),
    path('api/v1/', include('timing_adjustment.urls')),
]

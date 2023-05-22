from django.contrib import admin
from django.urls import include, path

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('users.urls')),
    path('api/v1/', include('temporary.urls')),
    path('api/v1/', include('feedback.urls')),
    path('api/v1/', include('vakantie.urls')),
    path('api/v1/', include('timing_adjustment.urls')),
]

urlpatterns += doc_urls

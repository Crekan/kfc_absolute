from django.urls import path

from temporary.views import (AdminView, ExportTemporaryDataView,
                             TemporaryCreateView, TemporaryView)

urlpatterns = [
    path('temporary/', TemporaryView.as_view(), name='temporary'),
    path('temporary/create/', TemporaryCreateView.as_view(), name='temporary_create'),
    path('temporary/view/', AdminView.as_view(), name='admin_view'),
    path('temporary/view/export/', ExportTemporaryDataView.as_view(), name='excel_export'),
]

from django.urls import path

from .views import (AdjustmentWorkingHoursCreateView,
                    AdjustmentWorkingHoursView, ShiftManagerCreateView,
                    ShiftManagerView)

urlpatterns = [
    path('manager/', ShiftManagerView.as_view(),
         name='manager_view'),
    path('manager/create/', ShiftManagerCreateView.as_view(),
         name='manager_create'),
    path('adjustments_to_working_hours/', AdjustmentWorkingHoursView.as_view(),
         name='adjustments_to_working_hours_view'),
    path('adjustments_to_working_hours/create/', AdjustmentWorkingHoursCreateView.as_view(),
         name='adjustments_to_working_hours_create'),
]

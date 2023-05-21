from django.contrib import admin

from .models import AdjustmentWorkingHours, ShiftManager

admin.site.register(ShiftManager)
admin.site.register(AdjustmentWorkingHours)

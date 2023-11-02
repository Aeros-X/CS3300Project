from django.contrib import admin
from .models import Employee, WorkShift, DayShift, Schedule

# Register your models here.
admin.site.register(Schedule)
admin.site.register(DayShift)
admin.site.register(WorkShift)
admin.site.register(Employee)

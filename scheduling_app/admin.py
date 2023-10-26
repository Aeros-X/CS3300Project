from django.contrib import admin
from .models import Student, Portfolio, Project, Employee, Work_Shift, Day_Shift, Schedule

# Register your models here.
admin.site.register(Student) 
admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(Schedule)
admin.site.register(Work_Shift)
admin.site.register(Day_Shift)
admin.site.register(Work_Shift)
admin.site.register(Employee)

from django.forms import ModelForm 
from .models import Employee, WorkShift, DayShift, Schedule
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#User form 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Create classes for schedule, day and work shift, and employees
class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ('year_cal', 'month_cal', 'week_cal')

class DayShiftForm(ModelForm):
    class Meta:
        model = DayShift
        fields = ('schedule', 'schedule_day', 'day_start_time', 'min_employees_per_department')

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'department')

class WorkShiftForm(ModelForm):
    class Meta:
        model = WorkShift
        fields = ('day_shift', 'start_time', 'duration', 'employee')
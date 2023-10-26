from django.forms import ModelForm 
from .models import Project, Portfolio, Employee, Work_Shift, Day_Shift, Schedule

#Create classes for schedule, day and work shift, and employees
class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ('year_cal', 'month_cal', 'week_cal')

class DayShiftForm(ModelForm):
    class Meta:
        model = Day_Shift
        fields = ('schedule', 'schedule_day', 'day_start_time', 'min_employees_per_department')

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'department')

class WorkShiftForm(ModelForm):
    class Meta:
        model = Work_Shift
        fields = ('day_shift', 'start_time', 'duration', 'employee')

#create class for project form 
class ProjectForm(ModelForm): 
    class Meta: 
        model = Project 
        fields = ('title', 'description') 

class PortfolioForm(ModelForm): 
    class Meta: 
        model = Portfolio 
        fields = ('title', 'is_active', 'about', 'contact_email') 
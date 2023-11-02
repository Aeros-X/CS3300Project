from django.urls import path 
from . import views

urlpatterns = [ 
#path function defines a url pattern 
#'' is empty to represent based path to app 
# views.index is the function defined in views.py 
# name='index' parameter is to dynamically create url 
# example in html <a href="{% url 'index' %}">Home</a>. 
path('', views.index, name='index'), 
path('schedules/', views.ScheduleListView.as_view(), name= 'schedules'), 
path('schedule/<int:pk>', views.ScheduleDetailView.as_view(), name='schedule-detail'),
path('schedule/create_schedule/', views.createSchedule, name='create_schedule'),
path('schedule/<int:schedule_id>/update_schedule/', views.updateSchedule, name='update_schedule'),
path('schedule/<int:schedule_id>/delete_schedule/', views.deleteSchedule, name='delete_schedule'),

path('dayshifts/', views.DayShiftListView.as_view(), name= 'dayshifts'),
path('dayshift/<int:pk>', views.DayShiftDetailView.as_view(), name= 'dayshift-detail'),
path('dayshift/create_dayshift/', views.createDayShift, name='create_dayshift'),
path('dayshift/<int:dayshift_id>/update_dayshift/', views.updateDayShift, name='update_dayshift'),
path('dayshift/<int:dayshift_id>/delete_dayshift/', views.deleteDayShift, name='delete_dayshift'),

path('workshifts/', views.WorkShiftListView.as_view(), name= 'workshifts'),
path('workshift/<int:pk>', views.WorkShiftDetailView.as_view(), name= 'workshift-detail'),
path('workshift/create_workshift/', views.createWorkShift, name='create_workshift'),
path('workshift/<int:workshift_id>/update_workshift/', views.updateWorkShift, name='update_workshift'),
path('workshift/<int:workshift_id>/delete_workshift/', views.deleteWorkShift, name='delete_workshift'),

path('employees/', views.EmployeeListView.as_view(), name= 'employees'), 
path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
path('employee/create_employee/', views.createEmployee, name='create_employee'),
path('employee/<int:employee_id>/update_employee/', views.updateEmployee, name='update_employee'),
path('employee/<int:employee_id>/delete_employee/', views.deleteEmployee, name='delete_employee')
]

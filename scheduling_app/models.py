from django.db import models
from django.db import models
from django.urls import reverse
from .teams_api import get_chat_messages
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
import calendar

#Create a message model
class Message(models.Model):
    message_id = models.CharField(max_length=255)
    content = models.TextField()

#Create a chat model
class Chat(models.Model):
    chat_id = models.CharField(max_length=255)
    messages = models.ManyToManyField(Message)

#Create the schedule model
class Schedule(models.Model): 

    #Get the variables for the date of the calendar
    year_cal = models.PositiveSmallIntegerField(blank= False)
    month_cal = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], blank= False)
    week_cal = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], blank=False)
    #Then make sure I can put a shift on each day

    #This code validates a week to make sure that we chose a number of weeks enough 
    def _validate_week(self):
        length_week_month = len(calendar.monthcalendar(self.year_cal, self.month_cal))
        if self.week_cal > length_week_month:
            raise ValidationError("Max weeks in " + str(self.month_cal) + ", " + str(self.year_cal) + " exceeded.")

    #This code saves the form and then calls the models original super
    def save(self, *args, **kwargs):
        self._validate_week()
        return super().save(*args, **kwargs)

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return str(self.week_cal) + ", " + str(self.month_cal)+ "/" + str(self.year_cal)
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('schedule-detail', args=[str(self.id)]) 
    
#Create the day shift model
class DayShift(models.Model):

    #Get the Schedule this is attached to, and create the important variables for said schedule
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, default = None, blank=False)
    schedule_day = models.PositiveSmallIntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(7)])
    day_start_time = models.TimeField(blank=False)
    min_employees_per_department = models.PositiveSmallIntegerField(default=1)

    def get_min(self):
        return self.min_employees_per_department

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return str(self.schedule) + ", " + str(self.schedule_day)
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('dayshift-detail', args=[str(self.id)]) 
    
#Create an employee model
class Employee(models.Model):

    #Get the name, and team that the employee is on
    name = models.CharField(max_length=200, blank=False)
    DEPARTMENT = (
        ('LDR', 'Leadership'),
        ('CC', 'Copy Center'),
        ('GM', 'General Merchandise'),
        ('SR', 'Shipping/Recieving'),
        ('EB', 'Entire Bookstore')
    )
    department = models.CharField(max_length=200, choices=DEPARTMENT, blank = False)

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return self.name
    
    def get_department(self):
        return self.department
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('employee-detail', args=[str(self.id)])

#Create the work shift model
class WorkShift(models.Model):

    #Get the day shift this corresponds to, and get the start time and shift duration, as well as the employee name and any notes needed
    day_shift = models.ForeignKey(DayShift, on_delete=models.CASCADE, default= None, blank= False)
    start_time = models.TimeField(blank=False)
    duration = models.DurationField(blank=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return str(self.employee) + str(self.day_shift)
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('workshift-detail', args=[str(self.id)])

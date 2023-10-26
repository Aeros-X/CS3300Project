from django.db import models
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
import calendar

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
        return str(self.week_cal) + str(self.month_cal) + str(self.year_cal)
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('schedule-detail', args=[str(self.id)]) 
    
#Create the day shift model
class Day_Shift(models.Model):

    #Get the Schedule this is attached to, and create the important variables for said schedule
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, default = None, blank=False)
    schedule_day = models.PositiveSmallIntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(7)])
    day_start_time = models.TimeField(blank=False)
    min_employees_per_department = models.PositiveSmallIntegerField(default=1)

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
        ('Leadership'),
        ('Copy Center'),
        ('General Merchandise'),
        ('Shipping/Recieving'),
        ('Entire Bookstore')
    )
    department = models.CharField(max_length=200, choices=DEPARTMENT, blank = False)

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return self.name
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('employee-detail', args=[str(self.id)])

#Create the work shift model
class Work_Shift(models.Model):

    #Get the day shift this corresponds to, and get the start time and shift duration, as well as the employee name and any notes needed
    day_shift = models.ForeignKey(Day_Shift, on_delete=models.CASCADE, default= None, blank= False)
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



# Create portfolio model
class Portfolio(models.Model): 

    #Provide the four variables for the portfolio model
    title = models.CharField(max_length=200) 
    contact_email = models.CharField("Contact Email", max_length=200) 
    is_active = models.BooleanField(default = False) 
    about = models.TextField(blank = True)

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return self.title 
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('portfolio-detail', args=[str(self.id)]) 

# Create project model
class Project(models.Model): 

    #Provide the variables for the project model
    title = models.CharField(max_length=200) 
    description = models.TextField(blank = False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default = None) 
    

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return self.title 
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('project-detail', args=[str(self.id)]) 

# Create student model
class Student(models.Model): 

#List of choices for major value in database, human readable name 
    MAJOR = ( 
        ('CSCI-BS', 'BS in Computer Science'), 
        ('CPEN-BS', 'BS in Computer Engineering'), 
        ('BIGD-BI', 'BI in Game Design and Development'), 
        ('BICS-BI', 'BI in Computer Science'), 
        ('BISC-BI', 'BI in Computer Security'), 
        ('CSCI-BA', 'BA in Computer Science'), 
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering') 
        ) 

    name = models.CharField(max_length=200) 
    email = models.CharField("UCCS Email", max_length=200) 
    major = models.CharField(max_length=200, choices=MAJOR, blank = False)
    portfolio = models.OneToOneField(Portfolio, on_delete = models.CASCADE, unique = True, default = None)
    

    #Define default String to return the name for representing the Model object." 
    def __str__(self): 
        return self.name 
    
    #Returns the URL to access a particular instance of MyModelName. 
    #if you define this method then Django will automatically 
    # add a "View on Site" button to the model's record editing screens in the Admin site 
    def get_absolute_url(self): 
        return reverse('student-detail', args=[str(self.id)]) 
"""    
# Model to represent the relationship between projects and portfolios. 
# Each instance of this model will have a reference to a Portfolio and a Project, 
# creating a many-to-many relationship between portfolios and projects. T 
class ProjectsInPortfolio(models.Model): 

    #deleting a portfolio will delete associate projects 
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE) 

    #deleting a project will not affect the portfolio 
    #Just the entry will be removed from this table 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 

    class Meta:
        #ensures that each project is associated with only one portfolio 
        unique_together = ('portfolio', 'project') 
"""
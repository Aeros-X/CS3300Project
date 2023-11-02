from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from scheduling_app.forms import ScheduleForm, EmployeeForm, DayShiftForm, WorkShiftForm
from .models import Schedule, WorkShift, DayShift, Employee
from datetime import datetime

def index(request): 
    #Get the current time stuff
    current_day = datetime.now()
    current_year = current_day.year
    current_month = current_day.month
    current_week = current_day.isocalendar()[1]

    #Set the day to be 1 so that we get the week number
    current_day = current_day.replace(day=1)
    first_week = current_day.isocalendar()[1]

    #Get the corresponding week number
    week_number = (current_week - first_week) + 1

    #Try to find a schedule that corresponds, otherwise, don't return anything
    try:
        schedule = Schedule.objects.get(year_cal = current_year, month_cal = current_month, week_cal = week_number)
    except Schedule.DoesNotExist:
        schedule = None

    #Return the render
    return render( request, 'scheduling_app/index.html', {'schedule_current_week':schedule})

"""
def portfolio_detail_view(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    project_list = Project.objects.filter(portfolio=portfolio)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio, 'project_list': project_list})

#Updates a portfolio when called
def updatePortfolio(request, portfolio_id):
    #Ensures we have the project
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    #If we are posting, updates the portfolio and saves the form
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio-detail', portfolio_id)
    #Otherwise we grab the original form to update
    else:
        form = PortfolioForm(instance=portfolio)

    return render(request, 'scheduling_app/portfolio_form.html', {'form': form, 'portfolio': portfolio})
"""
#Create a schedule
def createSchedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.save()

            # Redirect back to the portfolio detail page upon success
            return redirect('schedules')
    else:
        form = ScheduleForm()

    context = {
        'form': form,
    }
    return render(request, 'scheduling_app/schedule_form.html', context)    

#Create a schedule
def createDayShift(request):
    if request.method == 'POST':
        form = DayShiftForm(request.POST)
        if form.is_valid():
            dayshift = form.save(commit=False)
            dayshift.save()

            # Redirect back to the portfolio detail page upon success
            return redirect('dayshifts')
    else:
        form = DayShiftForm()

    context = {
        'form': form,
    }
    return render(request, 'scheduling_app/dayshift_form.html', context)

#Create a schedule
def createWorkShift(request):
    if request.method == 'POST':
        form = WorkShiftForm(request.POST)
        if form.is_valid():
            workshift = form.save(commit=False)
            workshift.save()

            # Redirect back to the portfolio detail page upon success
            return redirect('workshifts')
    else:
        form = WorkShiftForm()

    context = {
        'form': form,
    }
    return render(request, 'scheduling_app/workshift_form.html', context)

#Create a schedule
def createEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()

            # Redirect back to the portfolio detail page upon success
            return redirect('employees')
    else:
        form = EmployeeForm()

    context = {
        'form': form,
    }
    return render(request, 'scheduling_app/employee_form.html', context)


#Updates a schedule when called
def updateSchedule(request, schedule_id):
    #Ensures we have the project
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    #If we are posting, updates the project and saves the form
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule-detail', pk=schedule_id)
    #Otherwise we grab the original form to update
    else:
        form = ScheduleForm(instance=schedule)

    return render(request, 'scheduling_app/schedule_form.html', {'form': form, 'schedule': schedule})

#Updates a schedule when called
def updateDayShift(request, dayshift_id):
    #Ensures we have the project
    dayshift = get_object_or_404(DayShift, pk=dayshift_id)

    #If we are posting, updates the project and saves the form
    if request.method == 'POST':
        form = DayShiftForm(request.POST, instance=dayshift)
        if form.is_valid():
            form.save()
            return redirect('dayshift-detail', pk=dayshift_id)
    #Otherwise we grab the original form to update
    else:
        form = DayShiftForm(instance=dayshift)

    return render(request, 'scheduling_app/dayshift_form.html', {'form': form, 'dayshift': dayshift})

#Updates a schedule when called
def updateWorkShift(request, workshift_id):
    #Ensures we have the project
    workshift = get_object_or_404(WorkShift, pk=workshift_id)

    #If we are posting, updates the project and saves the form
    if request.method == 'POST':
        form = WorkShiftForm(request.POST, instance=workshift)
        if form.is_valid():
            form.save()
            return redirect('workshift-detail', pk=workshift_id)
    #Otherwise we grab the original form to update
    else:
        form = WorkShiftForm(instance=workshift)

    return render(request, 'scheduling_app/workshift_form.html', {'form': form, 'workshift': workshift})

#Updates a schedule when called
def updateEmployee(request, employee_id):
    #Ensures we have the project
    employee = get_object_or_404(Employee, pk=employee_id)

    #If we are posting, updates the project and saves the form
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-detail', pk=employee_id)
    #Otherwise we grab the original form to update
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'scheduling_app/employee_form.html', {'form': form, 'employee': employee})


#Deletes a project when called
def deleteSchedule(request, schedule_id):
    #Ensures we have the project
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    #If we are posting, we delete the project and jump back to portfolio-detail, otherwise, we show the website
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedules')
    else:
        return render(request, 'scheduling_app/schedule_delete.html', {'schedule': schedule})

#Deletes a project when called
def deleteDayShift(request, dayshift_id):
    #Ensures we have the project
    dayshift = get_object_or_404(DayShift, pk=dayshift_id)

    #If we are posting, we delete the project and jump back to portfolio-detail, otherwise, we show the website
    if request.method == 'POST':
        dayshift.delete()
        return redirect('dayshifts')
    else:
        return render(request, 'scheduling_app/dayshift_delete.html', {'dayshift': dayshift})

#Deletes a project when called
def deleteWorkShift(request, workshift_id):
    #Ensures we have the project
    workshift = get_object_or_404(WorkShift, pk=workshift_id)

    #If we are posting, we delete the project and jump back to portfolio-detail, otherwise, we show the website
    if request.method == 'POST':
        workshift.delete()
        return redirect('workshifts')
    else:
        return render(request, 'scheduling_app/workshift_delete.html', {'workshift': workshift})

#Deletes a project when called
def deleteEmployee(request, employee_id):
    #Ensures we have the project
    employee = get_object_or_404(Employee, pk=employee_id)

    #If we are posting, we delete the project and jump back to portfolio-detail, otherwise, we show the website
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')
    else:
        return render(request, 'scheduling_app/employee_delete.html', {'employee': employee})


#All of the views for schedule, dayshift, employees, workshift
class ScheduleListView(generic.ListView): 
    model = Schedule 
class ScheduleDetailView(generic.DetailView): 
    model = Schedule

class DayShiftListView(generic.ListView):
    model = DayShift
class DayShiftDetailView(generic.DetailView):
    model = DayShift

class EmployeeListView(generic.ListView):
    model = Employee
class EmployeeDetailView(generic.DetailView):
    model = Employee

class WorkShiftListView(generic.ListView):
    model = WorkShift
class WorkShiftDetailView(generic.DetailView):
    model = WorkShift
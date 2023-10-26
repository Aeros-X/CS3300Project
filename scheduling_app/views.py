from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from scheduling_app.forms import ProjectForm, PortfolioForm, ScheduleForm, EmployeeForm, DayShiftForm, WorkShiftForm
from .models import Student, Portfolio, Project, Schedule, Work_Shift, Day_Shift, Employee
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

def createProject(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page upon success
            return redirect('portfolio-detail', portfolio_id)
    else:
        form = ProjectForm()

    context = {
        'form': form,
        'portfolio': portfolio,
    }
    return render(request, 'scheduling_app/project_form.html', context)

#Updates a project when called
def updateProject(request, portfolio_id, project_id):
    #Ensures we have the project
    project = get_object_or_404(Project, pk=project_id)

    #If we are posting, updates the project and saves the form
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio-detail', portfolio_id)
    #Otherwise we grab the original form to update
    else:
        form = ProjectForm(instance=project)

    return render(request, 'scheduling_app/project_form.html', {'form': form, 'project': project})

#Deletes a project when called
def deleteProject(request, portfolio_id, project_id):
    #Ensures we have the project
    project = get_object_or_404(Project, pk=project_id)

    #If we are posting, we delete the project and jump back to portfolio-detail, otherwise, we show the website
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-detail', portfolio_id)
    else:
        return render(request, 'scheduling_app/project_delete.html', {'project': project})

#All of the views for schedule, dayshift, employees, workshift
class ScheduleListView(generic.ListView): 
    model = Schedule 
class ScheduleDetailView(generic.DetailView): 
    model = Schedule

class DayShiftListView(generic.ListView):
    model = Day_Shift
class DayShiftDetailView(generic.ListView):
    model = Day_Shift

class EmployeeListView(generic.ListView):
    model = Employee
class EmployeeDetailView(generic.DetailView):
    model = Employee

class WorkShiftListView(generic.ListView):
    model = Work_Shift
class WorkShiftDetailView(generic.DetailView):
    model = Work_Shift

class StudentListView(generic.ListView): 
    model = Student 
class StudentDetailView(generic.DetailView): 
    model = Student
class PortfolioListView(generic.ListView): 
    model = Portfolio
class PortfolioDetailView(generic.DetailView): 
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["project_list"] = Project.objects.filter(portfolio=self.object)
        return context

class ProjectListView(generic.ListView): 
    model = Project
class ProjectDetailView(generic.DetailView): 
    model = Project
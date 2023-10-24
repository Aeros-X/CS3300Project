from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from scheduling_app.forms import ProjectForm, PortfolioForm
from .models import Student, Portfolio, Project

def index(request): 
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True) 
    print("active portfolio query set", student_active_portfolios) 
    return render( request, 'scheduling_app/index.html', {'student_active_portfolios':student_active_portfolios})

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
from django.forms import ModelForm 
from .models import Project, Portfolio

#create class for project form 
class ProjectForm(ModelForm): 
    class Meta: 
        model = Project 
        fields = ('title', 'description') 

class PortfolioForm(ModelForm): 
    class Meta: 
        model = Portfolio 
        fields = ('title', 'is_active', 'about', 'contact_email') 
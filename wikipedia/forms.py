from django import forms
from .models import * 

# Create the various form models here 
class ProjectInputForm(forms.ModelForm): 
    """Form to collect the details of the article to be translated.
    
    Fields:
        article_title: The title of the Wikipedia article.
        target_language: The target language of the article.
    """
    
    class Meta: 
        model = Project
        fields = '__all__'
    


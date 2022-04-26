from django.shortcuts import render
from .forms import * 

# Create your views here.
def project_input_view(request):
    """View which holds the form to enter the details of the article and the target language.

    Args:
        request: request object

    Returns:
        Renders the page to be displayed
    """

    # Collect the form data 
    context = {}
    context['form'] = ProjectInputForm()

    return render(request, 'wikipedia/entry_page.html')
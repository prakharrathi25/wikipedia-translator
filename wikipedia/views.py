from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import * 

# Create your views here.
def project_input_view(request):
    """View which holds the form to enter the details of the article and the target language.

    Args:
        request: request object

    Returns:
        Renders the page to be displayed
    """
    
    # Set the form to be used for the project input page
    form = ProjectInputForm()

    # Handle the post request 
    if request.method == 'POST':
        
        # Set the form to be used for the project input page
        project_form = ProjectInputForm(request.POST)

        # Check if the form is valid
        if project_form.is_valid():

            # Save the form 
            project_form.save()
            messages.success(request, 'Project added successfully! Fetching the article data from Wikipedia...')
            return redirect('/project')

    # Render the form on the input page
    return render(request, 'input.html', {'form': form})


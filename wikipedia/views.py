from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import * 
from .models import * 

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
            return redirect('/translation?project_id=' + str(project_form.instance.id))

    # Render the form on the input page
    return render(request, 'input.html', {'form': form})


def translation_view(request): 
    """View which deals with collecting the summary and the translated text from the user

    Args:
        request: request object

    Returns:
        Renders the page to be displayed
    """

    # Handle the get request 
    if request.method == 'GET':

        # Get the project id from the URL
        project_id = request.GET.get('project_id')

        # Get the project details from the database
        project = Project.objects.get(id=project_id)

        # Collect the data about the project from the wikipedia API
        article_intro = project.get_article_summary()

        # Tokenize and save the article intro only if the article isn't already tokenized
        if project.is_tokenized == False: 
            result = Sentence.tokenize_intro_text(article_intro, project)
            project.is_tokenized = True
            project.save()
        
        # Get all the Sentence objects with a given project ID 
        result = Sentence.objects.filter(project_id=project.id)

        # if the article exists
        if article_intro: 

            # Render the translation page
            return render(request, 'translation.html', {'project': project,
                                                        'success': True,
                                                        'article_intro': article_intro,
                                                        'sentences': result})

        else: 
            # Render the error page
            return render(request, 'translation.html', {'project': project, 
                                                        'success': False}) 

    # Handle the post request
    if request.method == 'POST':

        pass 
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import * 
from .models import * 
from .decorators import *

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'admin'])
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
            # return redirect('/translation/' + str(project_form.instance.id)+'/')
            return redirect('manager/')

    # Render the form on the input page
    return render(request, 'input.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Annotator'])
def translation_view(request, pk): 
    """View which deals with collecting the summary and the translated text from the user

    Args:
        request: request object

    Returns:
        Renders the page to be displayed
    """

    # Handle the get request 
    if request.method == 'GET': 

        # Get the project details from the database
        project = Project.objects.get(id=pk)

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
            
            # check if the current user is a manager 
            is_manager = False
            if request.user.groups.filter(name='Manager').exists():
                is_manager = True

            # Render the translation page
            return render(request, 'translation.html', {'project': project,
                                                        'success': True,
                                                        'article_intro': article_intro,
                                                        'sentences': result, 
                                                        'manager': is_manager})

        else: 
            # Render the error page
            return render(request, 'translation.html', {'project': project, 
                                                        'success': False, 
                                                        'manager': is_manager})

    # Handle the post request
    if request.method == 'POST':

        # Get the project details from the database
        all_sentence_data = Sentence.objects.filter(project_id=pk)
        sentence_ids = [sentence.id for sentence in all_sentence_data]

        # Iterate through all the input fields in the form 
        for i in range(len(sentence_ids)): 
            
            # Get the translated text from the form
            try: 
                translated_text = request.POST[f"translated-{str(sentence_ids[i])}"]

                if translated_text: 
                    
                    # Update the Sentence object with the translated text
                    Sentence.objects.filter(id=sentence_ids[i]).update(translated_sentence=translated_text)
            
            except: 
                continue

        messages.success(request, "Your translations have been saved successfully!")
        return redirect('/translation/' + str(pk)+'/')
    
    else: 
        return redirect('/translation/' + str(pk)+'/')

@unauthenticated_user
def login_user(request): 

    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check the user group and redirect accordingly 
            if user.groups.filter(name='Manager').exists():
                return redirect('manager_dashboard')
            elif user.groups.filter(name='Annotator').exists():
                return redirect('annotator_dashboard')
            else:
                return redirect('login')
        
        else: 
            # Return the invalid users
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'login.html', {})

def logout_user(request): 
    
    # Log out the user and redirect to the log in page
    logout(request)

    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def manager_view(request):
    """View allow the user to view the projects and the annotators.

    Args:
        request (_type_): _description_

    Returns: 
    """

    
    # Handle form POST request
    if request.method == 'POST': 

        # Get the form data 
        project_id = request.POST['project_id']
        annotator_id = request.POST['annotator_id']

        # Get annotator object 
        new_annotator = User.objects.get(id=annotator_id)

        # Set the annotator for a particular project 
        Project.objects.filter(id=project_id).update(annotator=new_annotator)

    # Collect the data about the projects from the database
    projects = Project.objects.all()

    # Get the list of annotators
    annotators = User.objects.filter(groups__name='Annotator')

    return render(request, 'manager-dashboard.html', {'projects': projects, 
                                                      'annotators': annotators})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Annotator'])
def annot_dashboard_view(request):
    """View that allows the annotator to view the sentences that they can annotate.

    Args:
        request (_type_): _description_

    Returns: 
    """

    # Collect the projects that an annotator can annotate
    current_user = request.user
    user_id = current_user.id
    annotator_projects = Project.objects.filter(annotator_id=user_id)

    return render(request, 'annot-dashboard.html', {'annotator_projects': annotator_projects})
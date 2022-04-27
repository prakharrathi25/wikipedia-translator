from django.http import HttpResponse
from django.shortcuts import render, redirect

# Write the decorator functions for the various python functions in the views 
def unauthenticated_user(view_func): 
    """Function which disallows authenticated users to access the particular view and redirects them home page"""

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_roles=[]): 
    """Function which allows only the specified roles to access the particular view"""

    def decorator(view_func): 
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                html_output = """
                <p> You are not authorized to view this page! </p>
                <a href="logout/"> Go back to the login page. </a>
                """
                return HttpResponse(html_output)
        return wrapper_func
    return decorator
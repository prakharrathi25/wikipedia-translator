from django.urls import path, include
from .views import *

# Define routes for all the URL Paths
urlpatterns = [
    path('project', project_input_view(), name='main'),
]
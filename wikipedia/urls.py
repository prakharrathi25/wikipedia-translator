from django.urls import path, include
from . import views

# Define routes for all the URL Paths
urlpatterns = [
    path('project', views.project_input_view, name='main'),
]
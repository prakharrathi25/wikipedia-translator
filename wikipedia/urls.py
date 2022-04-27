from django.urls import path, include
from . import views

# Define routes for all the URL Paths
urlpatterns = [
    path('', views.project_input_view, name='main'),
    path('translation/<str:pk>/', views.translation_view, name='translation'),
]
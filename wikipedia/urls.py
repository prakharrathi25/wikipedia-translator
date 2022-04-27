from django.urls import path, include
from . import views

# Define routes for all the URL Paths
urlpatterns = [
    path('', views.project_input_view, name='main'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('translation/<str:pk>/', views.translation_view, name='translation'),
    path('manager/', views.manager_view, name='manager_dashboard'),
    path('annotator/', views.annot_dashboard_view, name='annotator_dashboard'),
]
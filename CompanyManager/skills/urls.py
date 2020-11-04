from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.all_skills, name = 'all_skills'),
]

from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employees, name = 'employees'),
    path('about/', views.test, name = 'about'),
]

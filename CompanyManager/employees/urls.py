from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employees, name = 'employees'),
    path('add/', views.addEmployee, name = 'addEmployee'),
    path('employee/<int:employees_pk/>', views.viewEmployee, name = 'viewEmployee'),
]

from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employees, name = 'employees'),
    path('add/', views.addEmployee, name = 'addEmployee'),
    path('employee/<int:employees_pk>', views.viewEmployee, name = 'viewEmployee'),
    path('employee/<int:employees_pk>', views.editEmployee, name = 'editEmployee'),
    path('employee/<int:employees_pk>/deleted', views.deleteEmployee, name = 'deleteEmployee'),
    path('employee/<int:employees_pk>/emergency_contact', views.viewEmergencyContact, name = 'viewEmergencyContact'),
]

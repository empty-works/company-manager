from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employees, name = 'employees'),
    path('add/', views.addEmployee, name = 'addEmployee'),
    path('add_successful', views.showSuccessAdd, name = 'showSuccessfulAdd'),
    path('employee/<int:employees_pk>', views.viewEmployee, name = 'viewEmployee'),
    path('employee/<int:employees_pk>/edit_employee', views.editEmployee, name = 'editEmployee'),
    path('employee/<int:employees_pk>/deleted', views.deleteEmployee, name = 'deleteEmployee'),
    path('employee/<int:employees_pk>/emergency_contact', views.viewEmergencyContact, name = 'viewEmergencyContact'),
    path('employee/<int:employees_pk>/view_all_experience', views.viewAllExperience, name = 'viewAllExperience'),
    path('employee/<int:employees_pk>/view_experience', views.viewExperience, name = 'viewExperience'),
    path('employee/<int:employees_pk>/edit_experience', views.editExperience, name = 'editExperience'),
    path('employee/<int:employees_pk>/view_all_skills', views.viewAllSkills, name = 'viewAllSkills'),
    path('employee/<int:employees_pk>/view_skill', views.viewSkill, name = 'viewSkill'),
    path('employee/<int:employees_pk>/edit_skill', views.editSkill, name = 'editSkill'),
]

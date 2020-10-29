from django.urls import path
from . import views

app_name = 'overview'

urlpatterns = [
    path('main_overview/', views.main, name = 'main_overview'),
]

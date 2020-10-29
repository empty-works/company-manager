from django.urls import path
from . import views

app_name = 'overview'

urlpatterns = [
    path('overview/', views.overview, name = 'overview'),
]

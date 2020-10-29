from django.urls import path
from . import views

app_name = 'overview'

urlpatterns = [
    path('main/', views.overview, name = 'overview'),
]

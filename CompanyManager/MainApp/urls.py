from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('help/', views.help, name = 'help'),
    path('about/', views.test, name = 'about'),
]

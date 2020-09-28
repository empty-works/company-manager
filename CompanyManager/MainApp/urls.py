from django.urls import path
from . import views

urlpatterns = [
    path('help/', views.help, name = 'help'),
    path('test/', views.test, name = 'test'),
]

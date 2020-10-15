from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
        path('', views.home, name = 'home'),
        path('signup/', views.signupuser, name = 'signupuser'),
        path('logout/', views.logoutuser, name = 'logoutuser'),
        path('login/', views.loginuseuser, name = 'loginuser'),
]

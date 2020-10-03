from django.urls import path

app_name = 'home'

urlpatterns = [
        path('home/', views.home, name = 'home'),
]

from django.urls import path
from . import views

app_name = 'blog' #Best practice to call any view more precisely. 

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]

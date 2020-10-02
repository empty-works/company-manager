from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    return render(request, 'blog/detail.html', {'id':blog_id})

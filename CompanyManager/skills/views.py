from django.shortcuts import render

def all_skills(request):
    return render(request, 'skills/all_skills.html')

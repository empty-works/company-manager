from django.shortcuts import render

def all_assignments(request):
    return render(request, 'assignments/all_assignments.html')

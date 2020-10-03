from django.shortcuts import render

def home(request):
    return render(request, 'company_manager/index.html')

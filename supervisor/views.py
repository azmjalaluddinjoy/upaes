from django.shortcuts import render

# Create your views here.


def add(request):

    return render(request, 'supervisor/add_supervisors.html')


def login(request):

    return render(request, 'supervisor/login.html')



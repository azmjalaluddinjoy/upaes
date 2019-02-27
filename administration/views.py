from django.shortcuts import render
from .models import Administration
# Create your views here.


def home(request):

    all_info = Administration.objects.all()
    for post in all_info:
        print(post)

    return render(request, 'administration/home.html', {'name': "Joy Bangla", 'district': "Dinajpur"})


def add_supervisors(request):

    return render(request, 'administration/add_supervisors.html')


def login(request):

    return render(request, 'administration/login.html')


def contact_developers(request):

    return render(request, 'administration/contact_developers.html')




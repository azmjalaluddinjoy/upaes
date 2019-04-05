from django.shortcuts import render
from .models import Supervisor
# Create your views here.


def home(request):

    return render(request, 'supervisor/home_supervisor.html')


def add(request):

    return render(request, 'supervisor/add_supervisors.html')


def add_request(request):
    supervisor_id = request.POST["supervisor_id"]
    faculty_name = request.POST["faculty_name"]
    designation = request.POST["designation"]
    web_page = request.POST["web_page"]
    email = request.POST["email"]
    password = request.POST["password"]

    add_request_supervisor = Supervisor(supervisor_id=supervisor_id, faculty_name=faculty_name, designation=designation,
                                        web_page=web_page, email=email, password=password)
    add_request_supervisor.save()
    return render(request, 'supervisor/add_supervisors.html')


def supervisor_list(request):

    supervisor = Supervisor.objects.all()

    return render(request, 'supervisor/supervisor_list.html', {'supervisors': supervisor})


def login(request):

    return render(request, 'supervisor/login.html')



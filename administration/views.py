from django.shortcuts import render
from .models import Administration
from project.models import ProjectPrimaryInfo
from student.models import Student
# Create your views here.


def home(request):

    all_info = Administration.objects.all()
    for post in all_info:
        print(post)

    return render(request, 'administration/home.html', {'name': "Joy Bangla", 'district': "Dinajpur"})


def all_project_status(request):
    all_basic_info = ProjectPrimaryInfo.objects.all()
    # if request.method == 'GET':
    #     student_info = Student.objects.get(studentId=pk)

    if request.method == 'POST':
        will_be_changed = ProjectPrimaryInfo.objects.filter(id='1')
        will_be_changed.approval = 'True'
    return render(request, 'administration/all_project_status.html', {'all_basic_info': all_basic_info})


def add_supervisors(request):

    return render(request, 'administration/add_supervisors.html')


def login(request):

    return render(request, 'administration/login.html')


def contact_developers(request):

    return render(request, 'administration/contact_developers.html')




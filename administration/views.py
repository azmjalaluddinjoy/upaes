from django.shortcuts import render

from supervisor.models import Supervisor
from .models import Administration
from project.models import ProjectPrimaryInfo
from student.models import Student
# Create your views here.


def home(request):
    count = ProjectPrimaryInfo.objects.count()
    all_basic_info = ProjectPrimaryInfo.objects.all()
    enrolling = Student.objects.count()
    supervisor_number = Supervisor.objects.count()
    # count = ProjectPrimaryInfo.objects.annotate(Count('approval'))
    all_info = Administration.objects.all()
    for post in all_info:
        print(post)

    return render(request, 'administration/home.html', {'all_basic_info': all_basic_info, 'name': "Joy Bangla",
                                                        'district': "Dinajpur",
                                                        'count': count, 'enrolling': enrolling, 'supervisor_number': supervisor_number})


def project(request, project_id):
    all_primary_info = ProjectPrimaryInfo.objects.get(pk=project_id)
    if all_primary_info.approval == 'False':
        # all_primary_info.approval = True
        all_primary_info.approval.update(True)
        # print(all_primary_info.approval)
    return render(request, 'administration/all_project_status.html')


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




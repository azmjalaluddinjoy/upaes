from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from supervisor.models import Supervisor
from .models import Administration
from project.models import ProjectPrimaryInfo, Supervised
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
    student_from = all_primary_info.s_id
    student = get_object_or_404(Student, studentId=student_from)
    this_student_project_basic_info = ProjectPrimaryInfo.objects.filter(s_id=student)
    supervisor_info = Supervisor.objects.all()
    supervising_info = Supervised.objects.filter(s_id=student)
    if all_primary_info.approval is False:
        all_primary_info.approval = True
        all_primary_info.save()
    if request.method == 'POST':
        supervisor = request.POST['supervisor_id']
        semester = request.POST['semester']
        requested_supervisor = Supervisor.objects.filter(supervisor_id=supervisor).first()
        save_request = Supervised(supervisor_id=requested_supervisor, s_id=student, semester=semester)
        save_request.save()
        return HttpResponseRedirect('/administration/home/')
    for this_student_project_basic_info in this_student_project_basic_info:
        project_name = this_student_project_basic_info.p_name
        category = this_student_project_basic_info.category
        student_id = this_student_project_basic_info.s_id
    return render(request, 'administration/all_project_status.html',
                      {'project_name': project_name, 'category': category, 'student_id': student_id,
                       'supervisor_info': supervisor_info, 'student': student, 'supervising_info': supervising_info})

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




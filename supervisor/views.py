from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Supervisor
from project.models import Supervised
from student.models import Student
# Create your views here.


def home(request):
    if request.session.get('supervisor_log'):
        supervisor_id = request.session.get('supervisor_log')
        supervised_students = Supervised.objects.filter(supervisor_id=supervisor_id)
        # supervised_students_information = Student.objects.filter(studentId=supervised_students)
        return render(request, 'supervisor/supervised_student.html', {'supervised_students': supervised_students})
    else:
        return render(request, 'supervisor/supervised_student.html')


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
    if request.method == 'POST':
        faculty_id = Supervisor.objects.get(supervisor_id=request.POST.get('emp_id'))
        if faculty_id.password == request.POST.get('password'):
            request.session['advising_log'] = faculty_id.supervisor_id
            print(faculty_id)
            return HttpResponseRedirect('/supervisor/home/')
        else:
            return HttpResponseRedirect('/supervisor/login/')
    return render(request, 'supervisor/login.html')


def logged_out(request):
    if request.session.get('advising_log'):
        del request.session['advising_log']
        return HttpResponseRedirect('/supervisor/login')
        # return HttpResponse('user loged out')
    else:
        return HttpResponse('somthing problem with login credentials !')



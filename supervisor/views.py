from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Supervisor
from project.models import Supervised, ProjectPrimaryInfo, DocumentType
from student.models import Student
# Create your views here.


def home(request):
    if request.session.get('advising_log'):
        supervisor_id = request.session.get('advising_log')
        print(supervisor_id)
        supervisor_object = get_object_or_404(Supervisor, supervisor_id=supervisor_id)
        students = supervisor_object.supervised_set.all()
        print(students)
        # supervised_students = Supervised.objects.filter(supervisor_id=supervised_object)
        # supervised_students_information = Student.objects.filter(studentId=supervised_students)
        return render(request, 'supervisor/supervised_student.html', {'students': students})
    else:
        return render(request, 'supervisor/supervised_student.html')


def add(request):

    return render(request, 'supervisor/add_supervisors.html')


def all_project(request):
    all_basic_info = ProjectPrimaryInfo.objects.all()
    return render(request, 'supervisor/all_project.html',{'all_basic_info': all_basic_info})


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
            if request.session.get('advising_log'):
                print('superviser loged in')
                return HttpResponseRedirect('/supervisor/home/')
            else:
                return HttpResponse('session not saved')
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


def add_new_type(request):
    if request.session.get('advising_log'):
        if request.method == 'POST':
            new_type = request.POST["add_new_document_type"]
            save_request = DocumentType(process_product_type=new_type)
            save_request.save()
            print(new_type)
    return render(request, 'supervisor/add_new_document_type.html')



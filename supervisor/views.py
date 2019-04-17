from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Supervisor
from project.models import Supervised, ProjectPrimaryInfo, DocumentType, ProductFile, Comment, Task
from student.models import Student
# Create your views here.


def home(request):
    if request.session.get('advising_log'):
        supervisor_id = request.session.get('advising_log')
        supervisor_object = get_object_or_404(Supervisor, supervisor_id=supervisor_id)
        students = supervisor_object.supervised_set.all()
        # supervised_students = Supervised.objects.filter(supervisor_id=supervised_object)
        # supervised_students_information = Student.objects.filter(studentId=supervised_students)
        return render(request, 'supervisor/supervised_student.html', {'students': students,
                                                                      'supervisor_profile_info': supervisor_object})
    else:
        return HttpResponseRedirect('/supervisor/login')


def task_assign(request, student_pk):
    supervised_info = Supervised.objects.get(pk=student_pk)
    student_info = get_object_or_404(Student, studentId=supervised_info.s_id)
    all_basic_info = ProjectPrimaryInfo.objects.filter(s_id=student_info)
    task_type = DocumentType.objects.all()
    all_assigned_task = Task.objects.filter(student=student_info)
    if request.method == 'POST':
        assigned_task = request.POST['task_type']
        marks_allocated = request.POST['marks_allocated']
        deadline = request.POST['deadline']
        task_request_type = get_object_or_404(DocumentType, process_product_type=assigned_task)
        task_save_request = Task(task_name=task_request_type, student=student_info, marks_allocated=marks_allocated, deadline=deadline)
        task_save_request.save()
    # student_from = supervised_info.s_id
    # student = get_object_or_404(Student, studentId=student_from)
    return render(request, 'supervisor/task_assign.html', {'supervised_info': supervised_info,
                                                           'student_info': student_info,
                                                           'task_type': task_type,
                                                           'all_basic_info': all_basic_info,
                                                           'all_assigned_task': all_assigned_task})


def evaluation(request, student_pk):
    # task_object = Task.objects.filter(pk=task_pk)
    task_info = Task.objects.get(pk=student_pk)

    print(task_info.task_name)
    print(student_pk)

    return render(request, 'supervisor/evaluate.html')


def add(request):

    return render(request, 'supervisor/add_supervisors.html')


def all_project(request):
    all_basic_info = ProjectPrimaryInfo.objects.all()
    return render(request, 'supervisor/all_project.html', {'all_basic_info': all_basic_info})


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


def review_comment(request):
    if request.session.get('advising_log'):
        all_document_type = DocumentType.objects.all()
        product_information = ProductFile.objects.all()
        all_comment = Comment.objects.all()
        # print(advising_comment)
        return render(request, 'supervisor/review_comments.html', {'all_document_type': all_document_type,
                                                                            'product_information': product_information,
                                                                            'all_comment': all_comment})


def profile(request):
    if request.session.get('advising_log'):
        supervisor_id = request.session.get('advising_log')
        profile_info = Supervisor.objects.filter(supervisor_id=supervisor_id)
        return render(request, 'supervisor/profile.html', {'profile_info': profile_info})

import datetime

from django.core.files.storage import FileSystemStorage
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post, Student, Values
from project.models import Category, ProjectPrimaryInfo, Comment, DocumentType, ProductFile, Supervised, Task
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.urls import reverse
# Create your views here.
from information.models import Districts


def home(request):
    if request.session.get('student_log'):
        new_task = 'Nill'
        student_id = request.session.get('student_log')
        student = get_object_or_404(Student, studentId=student_id)
        approval_status = 'You did not applied yet !'
        this_student_project_basic_info = ProjectPrimaryInfo.objects.filter(s_id=student)
        # if this_student_project_basic_info is not False:
        assigned_work = Task.objects.filter(student=student)
        present = timezone.now()
        for assigned_work in assigned_work:
            if assigned_work.deadline >= present:
                new_task = assigned_work
                print(assigned_work.task_name)
                print(assigned_work.deadline)
        for project_basic in this_student_project_basic_info:
            if project_basic.approval is False:
                approval_status = 'Pending'
            else:
                approval_status = 'Eligible'
        return render(request, 'student/home_student.html', {'approval_status': approval_status,
                                                             'new_task': new_task})
    else:
        return HttpResponseRedirect('/student/login')
        # return HttpResponse('User not loged in')


def apply_project(request):
    if request.session.get('student_log'):
        allcategory = Category.objects.all()

        return render(request, 'student/apply_project.html', {'allCategory': allcategory})


def insert(request):
    if request.session.get('student_log'):
        if request.method == 'POST':
            save_request_value = request.POST["data"]
            into_int = int(save_request_value)
            increased = into_int + 2
            database_save = Values(user_value=increased)
            database_save.save()
        data_value_increased = Values.objects.all()
        return render(request, 'student/insert.html', {'increased': data_value_increased})


def track_project(request):
    if request.session.get('student_log'):
        student_id = request.session.get('student_log')
        student = get_object_or_404(Student, studentId=student_id)
        all_basic_info = ProjectPrimaryInfo.objects.filter(s_id=student)
        marks = 0
        marks_get = 0
        for project_basic in all_basic_info:
            if project_basic.approval is True:
                approval_status = 'Eligible'
                assigned_work = Task.objects.filter(student=student)
                for assigned in assigned_work:
                    marks = assigned.marks_allowed + marks
                    marks_get = assigned.marks_allocated + marks_get
                product_document = ProductFile.objects.all()
                if request.method == 'POST':
                    document_type = request.POST['document_type']
                    student_id = request.session.get('student_log')
                    file_tracking_type = DocumentType.objects.filter(process_product_type=document_type).first()
                    uploaded_file = request.FILES['product_file']
                    product_file_save_request = ProductFile(student_id=student, file_tracking_type=file_tracking_type,
                                                            product_file=uploaded_file)
                    product_file_save_request.save()
                return render(request, 'student/track_project.html',
                                  {'all_basic_info': all_basic_info, 'assigned_work': assigned_work,
                                   'product_document': product_document, 'approval_status': approval_status,
                                   'marks': marks,
                                   'marks_get': marks_get})
            else:
                approval_status = 'Not eligible'
                return render(request, 'student/track_project.html', {'all_basic_info': all_basic_info,
                                                                      'approval_status': approval_status})

        return render(request, 'student/track_project.html', {'all_basic_info': all_basic_info})


def process_product_document(request):
    if request.session.get('student_log'):
        student_id = request.session.get('student_log')
        logged_student = get_object_or_404(Student, studentId=student_id)
        assigned_work = Task.objects.filter(student=logged_student)
        if request.method == 'POST':
            document_type = request.POST['document_type']
            request_type = get_object_or_404(DocumentType, process_product_type=document_type)
            product_information = ProductFile.objects.filter(file_tracking_type=request_type)
            this_student_product_information = product_information.filter(student_id=logged_student)
            student_comment = Comment.objects.filter(s_id=logged_student)

            # print(advising_comment)
            return render(request, 'student/process_product_view.html', {'assigned_work': assigned_work,
                                                                         'product_information': this_student_product_information,
                                                                         'all_comment': student_comment})

        return render(request, 'student/process_product_view.html', {'assigned_work': assigned_work})


def profile(request):
    if request.session.get('student_log'):
        student_id = request.session.get('student_log')
        profile_info = Student.objects.filter(studentId=student_id)
        return render(request, 'student/profile.html', {'profile_info': profile_info})


def authentication(request):

    return render(request, 'student/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/student/home/')
    else:
        form = SignUpForm()
    return render(request, 'student/signup.html', {'form': form})


def registration(request):

    return render(request, 'student/registration.html')


def add_registered_student(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    student_id = request.POST["studentId"]
    batch = request.POST["batch"]
    semester = request.POST["semester"]
    enroll_key = request.POST["enrollKey"]
    email = request.POST["email"]
    password = request.POST["password"]

    registered_req_student = Student(first_name=first_name, last_name=last_name, studentId=student_id,
                                               batch=batch, semester=semester, enrollKey=enroll_key, email=email, password=password)
    registered_req_student.save()
    # dis = Districts(name='abc',division_id=1)
    print("Hello, form is submitted")
    return render(request, "student/login.html")


def login_request(request):
    m = Student.objects.get(studentId=request.POST['student_id'])
    if m.password == request.POST['student_password']:
        request.session['student_log'] = m.studentId
        return HttpResponseRedirect('/student/home/')
    else:
        return HttpResponseRedirect('/student/registration')


def logged_out(request):
    if request.session.get('student_log'):
        del request.session['student_log']
        return HttpResponseRedirect('/student/login')
        # return HttpResponse('user loged out')
    else:
        return HttpResponse('somthing problem')

from django.core.files.storage import FileSystemStorage
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Student, Values
from project.models import Category, ProjectPrimaryInfo, Comment, DocumentType, ProductFile, Supervised
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.urls import reverse
# Create your views here.
from information.models import Districts


def home(request):
    if request.session.get('student_log'):
        student_id = request.session.get('student_log')
        student = get_object_or_404(Student, studentId=student_id)
        this_student_project_basic_info = ProjectPrimaryInfo.objects.filter(s_id=student)
        for project_basic in this_student_project_basic_info:
            if project_basic.approval is False:
                approval_status = 'Pending'
            else:
                approval_status = 'Eligible'
        return render(request, 'student/home_student.html', {'approval_status': approval_status})
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
        for project_basic in all_basic_info:
            if project_basic.approval is True:
                approval_status = 'Eligible'

            else:
                approval_status = 'Pending'
        all_document_type = DocumentType.objects.all()
        product_document = ProductFile.objects.all()
        if request.method == 'POST':
            document_type = request.POST['document_type']
            student_id = request.session.get('student_log')
            file_tracking_type = DocumentType.objects.filter(process_product_type=document_type).first()
            uploaded_file = request.FILES['product_file']
            # student = get_object_or_404(Student, studentId=student_id)
            product_file_save_request = ProductFile(student_id=student, file_tracking_type=file_tracking_type,
                                                    product_file=uploaded_file)
            product_file_save_request.save()
        return render(request, 'student/track_project.html', {'all_basic_info': all_basic_info, 'all_document_type': all_document_type,
                                                          'product_document': product_document})


def process_product_document(request):
    if request.session.get('student_log'):
        all_document_type = DocumentType.objects.all()
        if request.method == 'POST':
            student_id = request.session.get('student_log')
            logged_student = get_object_or_404(Student, studentId=student_id)
            document_type = request.POST['document_type']
            request_type = get_object_or_404(DocumentType, process_product_type=document_type)
            product_information = ProductFile.objects.filter(file_tracking_type=request_type)
            student_comment = Comment.objects.filter(s_id=logged_student)

            # print(advising_comment)
            return render(request, 'student/process_product_view.html', {'all_document_type': all_document_type,
                                                                         'product_information': product_information,
                                                                         'all_comment': student_comment})

        return render(request, 'student/process_product_view.html', {'all_document_type': all_document_type})


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

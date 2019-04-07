from django.core.files.storage import FileSystemStorage
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Student, Values
from project.models import Category, ProjectPrimaryInfo, Comment, DocumentType
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# Create your views here.
from information.models import Districts


def home(request):

    all_post = Post.objects.all()
    for post in all_post:
        print(post)

    return render(request, 'student/home_student.html', {'name': "Joy Bangla", 'district': "Dinajpur"})


def apply_project(request):
    allcategory = Category.objects.all()

    return render(request, 'student/apply_project.html', {'allCategory': allcategory})


def insert(request):
    if request.method == 'POST':
        save_request_value = request.POST["data"]
        into_int = int(save_request_value)
        increased = into_int + 2
        database_save = Values(user_value=increased)
        database_save.save()
    data_value_increased = Values.objects.all()
    return render(request, 'student/insert.html', {'increased': data_value_increased})


def track_project(request):
    all_basic_info = ProjectPrimaryInfo.objects.all()
    all_document_type = DocumentType.objects.all()
    # all_tracking_info = ProcessProductTracking.objects.filter(s_id=Student.objects.get(email=request.user.email))
    all_comment = Comment.objects.all()

    # if request.method == 'POST':
    #     if request.POST.get(request.FILES['srs']):
    #         srs_file = request.FILES['srs']
    #         fs = FileSystemStorage()
    #         srs_file_name = fs.save(srs_file.name, srs_file)
    #         uploaded_srs_file_url = fs.url(srs_file_name)
    #
    #     if request.POST.get(request.FILES['spmp']):
    #         spmp_file = request.FILES['spmp']
    #         fs = FileSystemStorage()
    #         spmp_file_name = fs.save(spmp_file.name, spmp_file)
    #         uploaded_spmp_file_url = fs.url(spmp_file_name)

    return render(request, 'student/track_project.html',
                  {'all_basic_info': all_basic_info, 'all_document_type': all_document_type,
                   'all_comment': all_comment})


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
        request.session["student_logged_in"] = m.id
        return HttpResponseRedirect('/student/home/')
    else:
        return HttpResponseRedirect('/student/registration')

    # except Member.DoesNotExist:
    #         return HttpResponse("Your username and password didn't match.")


#     studentId = request.POST["emp_id"]
#     password = request.POST["password"]
#     result = Student(studentId == studentId and password == password)
#     print("joy")
#     # if result == 1:
#     #     print("bangla")
# #    return render(request, "user_info/user_info.html")
#         return HttpResponseRedirect('/user/info/')


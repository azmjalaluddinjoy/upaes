from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Student
from project.models import Category, ProjectPrimaryInfo, ProcessProductTracking, Comment
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


def track_project(request):
    all_basic_info = ProjectPrimaryInfo.objects.all()
    all_tracking_info = ProcessProductTracking.objects.all()
    all_comment = Comment.objects.all()

    return render(request, 'student/track_project.html',
                  {'all_basic_info': all_basic_info, 'all_tracking_info': all_tracking_info,
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

        def set_color(request):
            if "favorite_color" in request.GET:

                # Create an HttpResponse object...
                response = HttpResponse("Your favorite color is now %s" % \
                                        request.GET["favorite_color"])

                # ... and set a cookie on the response
                response.set_cookie("favorite_color",
                                    request.GET["favorite_color"])

                return response

            else:
                return HttpResponse("You didn't give a favorite color.")


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


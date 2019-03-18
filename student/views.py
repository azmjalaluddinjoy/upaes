from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Student
from project.models import Category
# Create your views here.


def home(request):

    all_post = Post.objects.all()
    for post in all_post:
        print(post)

    return render(request, 'student/home_student.html', {'name': "Joy Bangla", 'district': "Dinajpur"})


def apply_project(request):
    allcategory = Category.objects.all()

    return render(request, 'student/apply_project.html', {'allCategory': allcategory})


def authentication(request):

    return render(request, 'student/login.html')


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
    print("Hello, form is submitted")
    return render(request, "student/login.html")


def login_request(request):

    m = Student.objects.get(studentId=request.POST['emp_id'])
    if m.password == request.POST['password']:
        # request.session['member_id'] = m.id
        return HttpResponseRedirect('/user/info/')

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


from django.shortcuts import render
from .models import Category, ProjectPrimaryInfo
# Create your views here.


def add_category(request):

    return render(request, 'project/add_category.html')


def add_category_request(request):
    category = request.POST['category']

    add_cat = Category(category=category)
    add_cat.save()
    return render(request, 'project/add_category.html')


def apply(request):
    category = request.POST['category_id']
    p_type = request.POST['projtype']
    p_name = request.POST['projectName']
    p_description = request.POST['projectDescription']
    vision = request.POST['projectVision']
    charter = request.POST['projectCharter']
    database_save = ProjectPrimaryInfo(category=category, p_type=p_type, p_name=p_name, p_description=p_description, vision=vision, charter=charter)
    database_save.save()
    return render(request, 'student/home_student.html')


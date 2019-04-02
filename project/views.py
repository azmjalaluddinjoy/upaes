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
    # allcategory = Category.objects.all()
    category_specification = request.POST['category_id']
    p_type = request.POST['projtype']
    p_name = request.POST['projectName']
    p_description = request.POST['projectDescription']
    vision = request.POST['projectVision']
    charter = request.POST['projectCharter']
    requested_category = Category.objects.filter(category=category_specification).first()
    database_save = ProjectPrimaryInfo(category=requested_category, p_type=p_type, p_name=p_name, p_description=p_description, vision=vision, charter=charter)
    database_save.save()
    # dis = Districts(name='abc',division_id=1)
    return render(request, 'student/home_student.html')


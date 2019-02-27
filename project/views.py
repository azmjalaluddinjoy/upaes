from django.shortcuts import render
from .models import Category
# Create your views here.


def add_category(request):

    return render(request, 'project/add_category.html')


def add_category_request(request):
    category = request.POST['category']
    projtype = request.POST['projtype']
    add_cat = Category(category=category, projtype=projtype)
    add_cat.save()
    return render(request, 'project/add_category.html')

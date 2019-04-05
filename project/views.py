import io
from datetime import datetime
from django.shortcuts import render
from .models import Category, ProjectPrimaryInfo, Evaluation, Student
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

# Create your views here.


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(file_name)
    return render(request, 'project/upload.html', {'uploaded_file_url': uploaded_file_url})


def html_to_pdf_view(request):
    evaluation_report = Evaluation.objects.all()
    for mark in evaluation_report:
        value = mark.supervisor_mark+mark.internal_01_mark+mark.internal_02_mark+mark.external_mark
    html_string = render_to_string('project/evaluation_sheet.html', {'evaluation_report': evaluation_report})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/evaluation_sheet.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('evaluation_sheet.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="evaluation_sheet.pdf"'
        return response
    #
    # return response


def project_primary_info_to_pdf(request):
    all_primary_info = ProjectPrimaryInfo.objects.all()
    html_string = render_to_string('project/basic_info.html', {'all_primary_info': all_primary_info})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/project_primary_info.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('project_primary_info.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="project_primary_info.pdf"'
        return response


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


def all_project(request):
    all_basic_info = ProjectPrimaryInfo.objects.all()
    return render(request, 'project/all_project.html', {'all_basic_info': all_basic_info})


def evaluation_status(request):
    evaluation_mark = Evaluation.objects.all()
    # value = evaluation_mark.supervisor_mark + evaluation_mark.internal_01_mark + evaluation_mark.internal_02_mark + evaluation_mark.external_mark
    return render(request, 'project/evaluation_status.html', {'evaluation_mark': evaluation_mark})



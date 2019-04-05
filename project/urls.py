from django.urls import path
from project import views


urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
    path('add_category_request/', views.add_category_request, name='add_category_request'),
    path('apply/', views.apply, name='apply'),
    path('all_project/', views.all_project, name='all_project'),
    path('evaluation_sheet/', views.html_to_pdf_view, name='evaluation_view_sheet'),
    path('evaluation_status/', views.evaluation_status, name='evaluation_status'),
    path('project_basic_info/', views.project_primary_info_to_pdf, name='project_primary_info_to_pdf'),
    path('upload/', views.upload, name='upload_testing'),

]

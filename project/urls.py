from django.urls import path
from project import views


urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
    path('add_category_request/', views.add_category_request, name='add_category_request'),
    path('apply/', views.apply, name='apply'),
    path('evaluation_sheet/', views.html_to_pdf_view, name='evaluation_view_sheet'),

]

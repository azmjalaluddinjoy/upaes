from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='administration'),
    path('add_supervisors/', views.add_supervisors, name='add_supervisors'),
    path('login/', views.login, name='login'),
    path('all_project_status/', views.all_project_status, name='all_project_status'),
    path('project/<project_id>/', views.project, name='project'),
    path('contact_developers/', views.contact_developers, name='contact_developers'),
]
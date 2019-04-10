from django.urls import path
from supervisor import views


urlpatterns = [
    path('home/', views.home, name='supervisor_home'),
    path('add/', views.add, name='supervisor_add'),
    path('add_request/', views.add_request, name='add_request'),
    path('supervisor_list', views.supervisor_list, name='supervisor_list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logged_out, name='logged_out'),
    path('projects/', views.all_project, name='all_project'),
    path('add_new_type/', views.add_new_type, name='add_new_type'),
    path('review_comments/', views.review_comment, name='review_comment'),


]

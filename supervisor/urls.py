from django.urls import path
from supervisor import views


urlpatterns = [
    path('add/', views.add, name='supervisor_add'),
    path('add_request/', views.add_request, name='add_request'),
    path('supervisor_list', views.supervisor_list, name='supervisor_list'),
    path('login/', views.login, name='login'),


]

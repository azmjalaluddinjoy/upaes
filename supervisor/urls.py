from django.urls import path
from supervisor import views


urlpatterns = [
    path('add/', views.add, name='supervisor_add'),
    path('login/', views.login, name='login'),

]
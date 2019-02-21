from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='administration'),
    path('add_supervisors/', views.add_supervisors, name='add_supervisors'),
    path('login/', views.login, name='login'),
]
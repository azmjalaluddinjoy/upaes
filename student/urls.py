from django.urls import path
from student import views


urlpatterns = [
    path('home/', views.home, name='student_home'),
    path('signup/', views.signup, name='signup'),
    path('apply_project/', views.apply_project, name='apply_project'),
    path('track_project/', views.track_project, name='track_project'),
    path('login/', views.authentication, name='student_login'),
    path('login_request/', views.login_request, name='student_login_request'),
    path('registration/', views.registration, name='student_registration'),
    path('insert/', views.insert, name='insert'),
    path('add_registered_student/', views.add_registered_student, name='add_registered_student')
]

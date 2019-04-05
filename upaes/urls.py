"""upaes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from student import views
admin.site.site_header = "University Project Approval & Evaluation System (Developer Admin)"
admin.site.site_title = "UPAES Admin Portal"
admin.site.index_title = "Welcome to UPAES"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls'), name='student'),
    path('user/', include('user_info.urls'), name='user'),
    path('administration/', include('administration.urls'), name='administration'),
    path('supervisor/', include('supervisor.urls'), name='supervisor'),
    path('project/', include('project.urls'), name='project'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_rooot=settings.MEDIA_ROOT)

from django.contrib import admin
from .models import Supervisor


class SupervisorAdminView(admin.ModelAdmin):
    list_display = ('supervisor_id', 'faculty_name', 'designation', 'web_page', 'email', 'password')
# Register your models here.


admin.site.register(Supervisor, SupervisorAdminView)


from django.contrib import admin
from .models import Post, Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'studentId', 'batch', 'semester', 'enrollKey', 'email', 'password')
# Register your models here.


admin.site.register(Post)
admin.site.register(Student, StudentAdmin)

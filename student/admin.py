from django.contrib import admin
from .models import Post, Student, Values


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'studentId', 'batch', 'semester', 'enrollKey', 'email', 'password')


# class ValuesAdmin(admin.ModelAdmin):
#     list_display = 'user_value'
# Register your models here.


admin.site.register(Post)
admin.site.register(Student, StudentAdmin)
admin.site.register(Values)

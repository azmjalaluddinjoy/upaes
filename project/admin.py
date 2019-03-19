from django.contrib import admin
from .models import Category, ProjectPrimaryInfo


class CategoryAdminView(admin.ModelAdmin):
    list_display = ('category_id', 'category')


class ProjectPrimaryInfoAdminView(admin.ModelAdmin):
    list_display = ('id', 'category', 'approval', 'p_type', 'p_name', 'p_description','vision', 'charter')
# Register your models here.


admin.site.register(Category, CategoryAdminView)
admin.site.register(ProjectPrimaryInfo, ProjectPrimaryInfoAdminView)
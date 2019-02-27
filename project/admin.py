from django.contrib import admin
from .models import Category


class CategoryAdminView(admin.ModelAdmin):
    list_display = ('category_id', 'category', 'projtype')
# Register your models here.


admin.site.register(Category, CategoryAdminView)


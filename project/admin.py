from django.contrib import admin
from .models import Category, ProjectPrimaryInfo, Comment, Evaluation, Supervised, ProductFile, DocumentType, Task


class CategoryAdminView(admin.ModelAdmin):
    list_display = ('category_id', 'category')


class ProjectPrimaryInfoAdminView(admin.ModelAdmin):
    list_display = ('id', 's_id', 'category', 'approval', 'p_type', 'p_name', 'p_description',
                    'vision', 'charter')


class CommentAdminView(admin.ModelAdmin):
    list_display = ('comment_id', 'process_product_type', 's_id', 'faculty_id', 'comment_title', 'comment')


class EvaluationAdminView(admin.ModelAdmin):
    list_display = ('eval_id', 'p_id', 's_id', 'plagiarism_documentation', 'plagiarism_source_code',
                    'supervisor_mark', 'internal_01_mark', 'internal_02_mark', 'external_mark')


class SupervisedAdminView(admin.ModelAdmin):
    list_display = ('supervisor_id', 's_id', 'semester')


class ProductFileAdminView(admin.ModelAdmin):
    list_display = ('student_id', 'file_tracking_type', 'product_file')


class TaskAdminView(admin.ModelAdmin):
    list_display = ('task_name', 'student', 'marks_allocated', 'marks_allowed', 'created_date', 'deadline')

# Register your models here.


admin.site.register(Category, CategoryAdminView)
admin.site.register(ProjectPrimaryInfo, ProjectPrimaryInfoAdminView)
# admin.site.register(ProcessProductTracking, ProcessProductTrackingAdminView)
admin.site.register(Comment, CommentAdminView)
admin.site.register(Evaluation, EvaluationAdminView)
admin.site.register(Supervised, SupervisedAdminView)
admin.site.register(ProductFile, ProductFileAdminView)
admin.site.register(DocumentType)
admin.site.register(Task, TaskAdminView)


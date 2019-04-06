from django.contrib import admin
from .models import Category, ProjectPrimaryInfo, ProcessProductTracking, Comment, Evaluation, Supervised


class CategoryAdminView(admin.ModelAdmin):
    list_display = ('category_id', 'category')


class ProjectPrimaryInfoAdminView(admin.ModelAdmin):
    list_display = ('id', 'category', 'approval', 'p_type', 'p_name', 'p_description',
                    'vision', 'charter')


class ProcessProductTrackingAdminView(admin.ModelAdmin):
    list_display = ('ppt_id', 's_id', 'p_id', 'srs', 'spmp', 'release_plan', 'iteration_plan',
                    'system_architecture_design', 'coding_standard', 'test_plan',
                    'test_case_specification', 'user_guide',
                    'system_video_documentation', 'video_demonstration', 'source_code_link')


class CommentAdminView(admin.ModelAdmin):
    list_display = ('comment_id', 'ppt_id', 'ppt_field', 's_id', 'faculty_id', 'comment_title', 'comment')


class EvaluationAdminView(admin.ModelAdmin):
    list_display = ('eval_id', 'p_id', 's_id', 'plagiarism_documentation', 'plagiarism_source_code',
                    'supervisor_mark', 'internal_01_mark', 'internal_02_mark', 'external_mark')


class SupervisedAdminView(admin.ModelAdmin):
    list_display = ('supervisor_id', 'category', 'p_id', 's_id', 'semester')

# Register your models here.


admin.site.register(Category, CategoryAdminView)
admin.site.register(ProjectPrimaryInfo, ProjectPrimaryInfoAdminView)
admin.site.register(ProcessProductTracking, ProcessProductTrackingAdminView)
admin.site.register(Comment, CommentAdminView)
admin.site.register(Evaluation, EvaluationAdminView)
admin.site.register(Supervised, SupervisedAdminView)


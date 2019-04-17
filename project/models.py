from django.db import models
from student.models import Student
from supervisor.models import Supervisor
from django.utils.timezone import now
# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class ProjectPrimaryInfo(models.Model):
    id = models.AutoField(primary_key=True)
    s_id = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)
    p_type = models.CharField(max_length=20)  # project or thesis
    p_name = models.CharField(max_length=50)
    p_description = models.CharField(max_length=500)
    vision = models.CharField(max_length=500)
    charter = models.CharField(max_length=250)

    def __str__(self):
        return self.p_name


# class ProcessProductTracking(models.Model):
#     ppt_id = models.AutoField(primary_key=True)
#     s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     p_id = models.ForeignKey(ProjectPrimaryInfo, on_delete=models.CASCADE)
#     srs = models.CharField(blank=True, null=True, max_length=200)
#     spmp = models.CharField(blank=True, null=True, max_length=200)
#     release_plan = models.CharField(blank=True, null=True, max_length=200)
#     iteration_plan = models.CharField(blank=True, null=True, max_length=200)
#     system_architecture_design = models.CharField(blank=True, null=True, max_length=200)
#     coding_standard = models.CharField(blank=True, null=True, max_length=200)
#     test_plan = models.CharField(blank=True, null=True, max_length=200)
#     test_case_specification = models.CharField(blank=True, null=True, max_length=200)
#     user_guide = models.CharField(blank=True, null=True, max_length=200)
#     system_video_documentation = models.CharField(blank=True, null=True, max_length=200)
#     video_demonstration = models.CharField(blank=True, null=True, max_length=200)
#     source_code_link = models.CharField(blank=True, null=True, max_length=200)
#
#     def __str__(self):
#         return '%s' % self.ppt_id


class DocumentType(models.Model):
    process_product_type = models.CharField(blank=True, default=None, null=True, max_length=50)

    def __str__(self):
        return '%s' % self.process_product_type


class ProductFile(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    file_tracking_type = models.ForeignKey(DocumentType, default=None, on_delete=models.CASCADE)
    product_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.product_file


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    process_product_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    s_id = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(Supervisor, blank=True, null=True, on_delete=models.CASCADE)
    comment_title = models.CharField(blank=True, null=True, max_length=500)
    comment = models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return '%s' % self.comment_id


class Evaluation(models.Model):
    eval_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(ProjectPrimaryInfo, on_delete=models.CASCADE)
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    plagiarism_documentation = models.IntegerField(blank=True, null=True)
    plagiarism_source_code = models.IntegerField(blank=True, null=True)
    supervisor_mark = models.IntegerField(blank=True, null=True)
    internal_01_mark = models.IntegerField(blank=True, null=True)
    internal_02_mark = models.IntegerField(blank=True, null=True)
    external_mark = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.eval_id


class Supervised(models.Model):
    supervisor_id = models.ForeignKey(Supervisor, null=True, blank=True, on_delete=models.CASCADE)
    s_id = models.ForeignKey(Student, null=True, blank=True,  on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, null=True, blank=True, )

    def __str__(self):
        return '%s' % self.s_id


class Task(models.Model):
    task_name = models.ForeignKey(DocumentType, null=False, blank=False, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    marks_allocated = models.IntegerField(blank=True, null=True, default=10)
    marks_allowed = models.IntegerField(blank=True, null=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.task_name


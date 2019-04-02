from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class ProjectPrimaryInfo(models.Model):
    id = models.AutoField(primary_key=True)
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
#     ppt_id =
#     s_id =
#     p_id =
#     srs = models.CharField(max_length=200)
#     spmp = models.CharField(max_length=200)
#     release_plan = models.CharField(max_length=200)
#     iteration_plan = models.CharField(max_length=200)
#     system_architecture_design = models.CharField(max_length=200)
#     coding_standard = models.CharField(max_length=200)
#     test_plan = models.CharField(max_length=200)
#     test_case_specification = models.CharField(max_length=200)
#     user_guide = models.CharField(max_length=200)
#     system_video_documentation = models.CharField(max_length=200)
#     video_demonstration = models.CharField(max_length=200)
#     source_code_link = models.CharField(max_length=200)
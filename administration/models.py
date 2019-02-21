from django.db import models

# Create your models here.


class Administration(models.Model):

    emp_id = models.IntegerField()
    full_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    web_page = models.CharField(max_length=300)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email

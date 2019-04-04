from django.db import models
# import django_tables2 as tables

# Create your models here.


# class SimpleTable(tables.Table):
#     class Meta:
#         model = Simple


class Supervisor(models.Model):

    supervisor_id = models.IntegerField()
    faculty_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    web_page = models.URLField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=13)

    def __str__(self):
        return self.supervisor_id
        # return '%s %s %s %s' % (self.supervisor_id, self.faculty_name, self.designation, self.email)


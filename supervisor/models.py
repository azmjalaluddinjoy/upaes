from django.db import models

# Create your models here.


class Supervisor(models.Model):

    supervisor_id = models.IntegerField()
    faculty_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    web_page = models.URLField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=13)

    def __str__(self):
        # return self.faculty_name
        return '%s %s %s %s' % (self.supervisor_id, self.faculty_name, self.designation, self.email)


from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    studentId = models.CharField(max_length=30)
    batch = models.CharField(max_length=20)
    semester = models.CharField(max_length=30)
    enrollKey = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.studentId


from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    projtype = models.CharField(max_length=30)

    def __str__(self):
        return self.category

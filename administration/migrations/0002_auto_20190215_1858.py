# Generated by Django 2.1.6 on 2019-02-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='emp_id',
            field=models.IntegerField(),
        ),
    ]

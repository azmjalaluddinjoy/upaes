# Generated by Django 2.1.6 on 2019-04-08 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190407_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervised',
            name='category',
        ),
    ]

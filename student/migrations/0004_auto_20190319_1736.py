# Generated by Django 2.1.6 on 2019-03-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190319_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

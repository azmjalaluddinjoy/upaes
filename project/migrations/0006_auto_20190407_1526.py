# Generated by Django 2.1.6 on 2019-04-07 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20190407_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='faculty_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='supervisor.Supervisor'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='s_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]

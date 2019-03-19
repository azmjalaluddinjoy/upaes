# Generated by Django 2.1.6 on 2019-03-19 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190319_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPrimaryInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('approval', models.BooleanField(default=False)),
                ('p_type', models.CharField(max_length=20)),
                ('p_name', models.CharField(max_length=50)),
                ('p_description', models.CharField(max_length=500)),
                ('vision', models.CharField(max_length=500)),
                ('charter', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]

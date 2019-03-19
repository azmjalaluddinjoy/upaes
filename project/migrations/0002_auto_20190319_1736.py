# Generated by Django 2.1.6 on 2019-03-19 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('approval', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=20)),
                ('p_name', models.CharField(max_length=50)),
                ('p_description', models.CharField(max_length=30)),
                ('vision', models.CharField(max_length=20)),
                ('charter', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='projtype',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Category'),
        ),
    ]
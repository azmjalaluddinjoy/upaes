# Generated by Django 2.1.6 on 2019-02-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_id', models.IntegerField()),
                ('faculty_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('web_page', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=13)),
            ],
        ),
    ]

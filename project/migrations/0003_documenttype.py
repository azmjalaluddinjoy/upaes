# Generated by Django 2.1.6 on 2019-04-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_productfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_product_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

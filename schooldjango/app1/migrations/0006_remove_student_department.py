# Generated by Django 3.0.1 on 2020-01-17 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200117_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
    ]

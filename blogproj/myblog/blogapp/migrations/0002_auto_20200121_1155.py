# Generated by Django 3.0.1 on 2020-01-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
    ]

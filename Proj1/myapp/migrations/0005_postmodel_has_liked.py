# Generated by Django 3.0.1 on 2019-12-24 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_postmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='has_liked',
            field=models.BooleanField(default=False),
        ),
    ]

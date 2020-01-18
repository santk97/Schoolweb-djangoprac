# Generated by Django 3.0.1 on 2020-01-17 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200117_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dept2',
            field=models.CharField(default='cse', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d', to='app1.Dept'),
        ),
    ]

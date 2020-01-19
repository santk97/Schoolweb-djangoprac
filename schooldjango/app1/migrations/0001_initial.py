# Generated by Django 3.0.1 on 2020-01-17 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('rollno', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=150)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Dept')),
            ],
        ),
    ]
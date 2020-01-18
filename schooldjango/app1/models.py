from django.db import models

# Create your models here.
class Dept(models.Model):
    #choice=(('1','CSE'),('ECE','ECE'),('ECE','ECE'),('MECHANICAL','MECHANICAL'),('MECHATRONICS','MECHATRONICS'),('Applied','Applied'))
    dept_name=models.CharField(max_length=250)

    def __str__(self):
        return self.dept_name

class Student(models.Model):
    name=models.CharField(max_length=150)
    rollno=models.IntegerField(unique=True,null=False)
    #dept2=models.CharField(max_length=200)
    department=models.ForeignKey(Dept,on_delete=models.CASCADE,default='1')
    city=models.CharField(max_length=150)

    def __str__(self):
        return self.name
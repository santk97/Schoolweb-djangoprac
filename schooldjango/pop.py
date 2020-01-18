import  os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','schooldjango.settings')

import django
django.setup()
from app1.models import Dept, Student
from faker import Faker
import random

gen=Faker()
dep_list=['CSE','ECE','CIVIL','MECHANICAL','MECHATRONICS','Applied']

def put_Dep():
    t=Dept.objects.get_or_create(dept_name=random.choice(dep_list))[0]
    t.save()
    return t

def put_values(n):
    for x in range(n):
        dept=put_Dep()
        name=gen.name()
        rollno=x+1
        city=gen.city()
        dep=Dept.objects.get_or_create(dept_name=dept)
        Student.objects.get_or_create(name=name,rollno=rollno,city=city,department=dept)

if __name__=='__main__':
    print('populating script')
    put_values(20)
    print('done')
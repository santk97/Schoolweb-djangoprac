from django.forms import ModelForm , ModelChoiceField
from django import forms
from .models import Student,Dept
# simple django froms works
class Reg_form(forms.ModelForm):

    department=forms.ModelChoiceField(queryset=Dept.objects.all(),to_field_name='dept_name')
    #to_field_name tells us where to look it could be id. dept_name and somwething else when wroking with a froeign key
    class Meta():
        model=Student
        fields=('name','rollno','city','department')

class filter_form(forms.Form):
    filter_dept=forms.ModelChoiceField(queryset=Dept.objects.all(),to_field_name='dept_name')



'''class Deptmenumodel(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Department #%s) %s" % (obj.id, obj.dept_name)

class Reg_form(forms.ModelForm):
    department = Deptmenumodel(queryset=Dept.objects.all())

    class Meta:
        model = Student
        fields = '__all__'''



'''class Reg_form(ModelForm):

    class Meta():
        model=Student
        fields=('name','rollno','city','department')'''
from django import forms
from .models import  Student
class Reg_form(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'
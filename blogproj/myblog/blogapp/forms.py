from django import forms
from .models import  Blog

class Blog_form(forms.ModelForm):
    text=forms.Textarea()
    class Meta():
        model=Blog
        fields=('author','title','text')
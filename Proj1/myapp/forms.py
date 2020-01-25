from django import  forms
from .models import User_model,PostModel

class User_Signupform(forms.ModelForm):
    class Meta():
        model=User_model
        fields=['name','username','email','password','is_active']


class User_Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image', 'caption']
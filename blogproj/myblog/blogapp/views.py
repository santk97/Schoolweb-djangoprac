from django.shortcuts import render,redirect
from .models import Blog
from .forms import  Blog_form
# Create your views here.
def home(request):
    blogs=Blog.objects.all()

    return render(request,'home.html',{'blogs':blogs})

def write_blog(request):
    if request.method=='POST':
        form=Blog_form(request.POST)
        if form.is_valid():
            print('Form is valid')
            print(form.cleaned_data['title'])
            form.save(commit=True)
            print('form is saved')
            return redirect('/')
        else:
            print(form.errors)
    else:
        form=Blog_form()
    return render(request,'write.html',{'form':form})
from django.shortcuts import render,redirect
from .forms import  Reg_form
from .models import  Student
# Create your views here.
def index(request):
    return  render(request,'index.html')

def reg_Stud(request):
    if request.method=='POST':
        form=Reg_form(request.POST)
        if form.is_valid():
            print("form succesfull")
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
    else:
        return  render(request,'reg.html')

def stud(request):
    obj=Student.objects.all()
    return render(request,'stud.html',{'studs':obj})
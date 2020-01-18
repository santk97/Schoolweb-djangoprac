from django.shortcuts import render,redirect
from .models import Dept,Student
from .forms import Reg_form,filter_form
# Create your views here.
def index(request):
    return render(request,'home.html')

def list_Stud(request):
    stud=Student.objects.order_by('rollno')
    dept=Dept.objects.all()
    if request.method=='POST':
        fform=filter_form(request.POST)
        if fform.is_valid():
            print(fform.cleaned_data['filter_dept'])
            selected_dept=fform.cleaned_data['filter_dept']
            stud=Student.objects.filter(department=selected_dept)
            print(stud)
            return render(request, 'studentlist.html', {'stud': stud, 'dept': dept,'selected':selected_dept})
        else:
            print(fform.errors)
            return render(request, 'studentlist.html', {'stud': stud, 'dept': dept})
    else:

        return render(request,'studentlist.html',{'stud':stud,'dept':dept})

def deplist(request):
    dept=Dept.objects.all()
    return render(request,'deplist.html',{'dept':dept})

def register(request):
    dept = Dept.objects.all()
    if request.method=='POST':
        reg_form=Reg_form(request.POST)
        print(reg_form)
        if reg_form.is_valid():
            print(reg_form.cleaned_data['name'])
            print(reg_form.cleaned_data['department'])
            reg_form.save(commit=True)
            return redirect('/')

        else:
            print('Form invalid')
            print(reg_form.errors)

            return render(request, 'register.html', {'dept': dept, 'error': reg_form.errors})
    else :
        reg_form=Reg_form()
    return render(request, 'register.html', {'dept': dept})
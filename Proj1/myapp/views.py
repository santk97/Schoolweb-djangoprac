from django.shortcuts import render,HttpResponse,redirect
from .models import  User_model,session_token, PostModel
from .forms import User_Signupform,User_Loginform,PostForm
from django.contrib.auth.hashers import make_password ,check_password

from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.


def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'myapp/index.html')

def signup(request):
    if request.method=='POST':
        signup_form=User_Signupform(request.POST)
        if signup_form.is_valid():
            print("Form succesfulll")
            name=signup_form.cleaned_data['name']
            username=signup_form.cleaned_data['username']
            email=signup_form.cleaned_data['email']
            password=signup_form.cleaned_data['password']
            obj=User_model(name = name, username = username, password = make_password(password), email = email)
            obj.save()
            print('User data is saved')
            try:
                subject='Activation'
                message='You just signed Up for InstaCLone ....'+\
                       '.click on the link below to get your account activated \n\n '+\
                        'http://127.0.0.1:8000/myapp/activate/?username='+(username)
                to=[email]
                sender='ssantk97@gmail.com'
                send_mail(subject, message, sender, to, fail_silently=False)
                print (' Activation mail sent ')
            except Exception as e:
                print(e)
                print (' network error in sending the mail')
            return render(request,'myapp/verification_sent.html',context={'email':email})
        else:
            print("Form Failed")
            print(signup_form.errors)
    else:
        signup_form=User_Signupform()
    return render(request,'myapp/sign_up.html',context={'form':signup_form})

def activate(request):
    user = request.GET.get('username')
    user_obj = User_model.objects.filter(username=user).first()
    print(user_obj)
    print(user_obj.name)
    print(user_obj.email)
    print(user_obj.is_active)
    # changing the is active field to true for activated users
    if user_obj.is_active == False:
        user_obj.is_active = True
        user_obj.save()
    else:
        print(' user has been alreay activated')
    return render(request, 'myapp/activate.html', {'user': user_obj.name})



def login(request):
    if request.method=='POST':
        login_form=User_Loginform(request.POST)
        if login_form.is_valid():
            print("Form succesfull")
            print(login_form)
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            print(username,password)
            obj=User_model.objects.filter(username=username).first()
            print(obj)
            if  obj==None:
                print("user not found")
                return render(request, 'myapp/Login.html', {'error': 'user doesnot exist '})
            else:
                # print(obj.password)
                if check_password(password,obj.password):
                    print("Login Succesfull")
                    token = session_token(username=obj)
                    token.create_token()
                    token.save()
                    response = redirect('/myapp/dashboard/')
                    print( response)
                    response.set_cookie(key='session_token', value=token.token)
                    print('cookie created')
                    return response
                else:
                    print('Wrong PAssword')
                    return render(request, 'myapp/Login.html', {'error': 'Wrong PAssword '})
        else:
            print("Form Failed")
            print(login_form.errors)
            return render(request, 'myapp/Login.html', {'error':login_form.errors})
    else:
        login_form=User_Loginform()
    return render(request,'myapp/Login.html',{})

#this method checks if user is alredy login or has a cookie created
def check_validation(request):
    if request.COOKIES.get('session_token'):
        session=session_token.objects.filter(token=request.COOKIES.get('session_token')).first()
        print(request.COOKIES.get('session_token'))
        if session:
            return session.username
    else:
            return None

def dash(request):
    obj=check_validation(request)
    if obj:
        posts = PostModel.objects.all().order_by('-created_on')
        print(posts)
        return render(request, 'myapp/dash.html', {'posts': posts})
    else:
            return redirect('/login/')

def create_post(request):
    obj=check_validation(request)
    if obj:
        if request.method=='POST':
            postform=PostForm(request.POST,request.FILES)
            if postform.is_valid():
                image = postform.cleaned_data.get('image')
                caption = postform.cleaned_data.get('caption')
                post = PostModel(user=obj, image=image, caption=caption)
                post.save()
                path = post.image.url
                post.image_url = path
                post.save()
                return redirect('/myapp/dashboard/')
            else:
                print('form failed')
                print(postform.errors)
                return  render(request,'myapp/create_post.html',{'form':postform,'error':postform.errors})
        else:
            postform=PostForm()
            return  render(request,'myapp/create_post.html',{'form':postform})
    else:
        return redirect('/login/')

def logout(request):
    HttpResponse("<h1> Logging out .....</h1>")
    user=check_validation(request)
    if user:
        token = session_token.objects.filter(username=user)
        token.delete()
        return redirect('/myapp/')
    else:
        return  redirect('/myapp/login/')



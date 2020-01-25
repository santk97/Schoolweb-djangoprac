from django.conf.urls import url
from .views import  index,signup,login,dash,logout,activate,create_post

urlpatterns=[

    url(r'^$',index),
    url(r'^signup',signup,name='SIGNUP'),
url(r'^login',login,name='LOGIN'),
    url(r'^dashboard',dash,name='DASHBOARD'),
    url(r'^logout',logout,name='LOGOUT'),
    url(r'^activate',activate,name='ACTIVATE'),
    url(r'create_post',create_post,name='CREATE')

]



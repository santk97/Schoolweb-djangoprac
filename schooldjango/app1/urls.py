from django.contrib import admin
from django.urls import path,include
from .views import register,list_Stud,deplist,indiv,delte

urlpatterns = [
path('register/',register),
path('list_students/',list_Stud),
path('list_department/',deplist),
    path('individual/',indiv),
    path('delete/',delte)
]
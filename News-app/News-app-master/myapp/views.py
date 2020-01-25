# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
import requests

base_url='https://newsapi.org/v2/'
api_key='e39b29c853e642fd800d94b8fc363586'
title=[]
description=[]




# Create your views here.
def business(request):
    request_url = (base_url + '/top-headlines?country=in&category=business&apiKey=%s' % (api_key))
    headlines = requests.get(request_url).json()
    for headline in headlines['articles']:
        title.append(headline['title'])
        description.append(['description'])
    return render(request,'myapp/details.html',{'headlines':headlines})

def entertainment(request):
    request_url = (base_url + '/top-headlines?country=in&category=entertainment&apiKey=%s' % (api_key))
    headlines = requests.get(request_url).json()
    for headline in headlines['articles']:
        title.append(headline['title'])
        description.append(['description'])
    return render(request,'myapp/details.html',{'headlines':headlines})

def sports(request):
    request_url = (base_url + '/top-headlines?country=in&category=sports&apiKey=%s' % (api_key))
    headlines = requests.get(request_url).json()
    for headline in headlines['articles']:
        title.append(headline['title'])
        description.append(['description'])
    return render(request,'myapp/details.html',{'headlines':headlines})

def health(request):
    request_url = (base_url + '/top-headlines?country=in&category=health&apiKey=%s' % (api_key))
    headlines = requests.get(request_url).json()
    for headline in headlines['articles']:
        title.append(headline['title'])
        description.append(['description'])
    return render(request,'myapp/details.html',{'headlines':headlines})

def science(request):
    request_url = (base_url + '/top-headlines?country=in&category=science&apiKey=%s' % (api_key))
    headlines = requests.get(request_url).json()
    for headline in headlines['articles']:
        title.append(headline['title'])
        description.append(['description'])
    return render(request,'myapp/details.html',{'headlines':headlines})

def technology(request):
    request_url = (base_url + '/top-headlines?country=in&category=technology&apiKey=%s' % (api_key))
    headlines = requests.get(request_url).json()
    for headline in headlines['articles']:
        title.append(headline['title'])
        description.append(['description'])
    return render(request,'myapp/details.html',{'headlines':headlines})

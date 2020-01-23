"""cbvproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.Cbview.as_view(),name='Home'),
    url(r'^index',views.Indexview.as_view(),name='Index'),
    url(r'^brands',views.BrandListview.as_view(),name='Brands'),
    url(r'^products',views.ProductListview.as_view(),name='Products'),
    url(r'^(?P<pk>\d+)/$',views.BrandDetailView.as_view(),name='brand_detail'),
    url(r'^\d/+(?P<pk>\d+)/$',views.ProductDetailView.as_view(),name='product_detail'),


]

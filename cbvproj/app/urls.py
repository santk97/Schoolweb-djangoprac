from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^brands',views.BrandListview.as_view(),name='Brands'),
    url(r'^products',views.ProductListview.as_view(),name='Products'),
    url(r'^(?P<pk>\d+)/$',views.BrandDetailView.as_view(),name='brand_detail'),
    url(r'^\d/+(?P<pk>\d+)/$',views.ProductDetailView.as_view(),name='product_detail'),
    url(r'createbrand/',views.CreateBrandView.as_view(),name='CreateBrand'),
    url(r'(?P<pk>\d+)/createproduct/',views.CreateProductView.as_view(),name='CreateProduct'),
    url(r'deletebrand/(?P<pk>\d)',views.DeleteBrandView.as_view(),name='DeleteBrand'),
    url(r'updateproduct/(?P<pk>\d)',views.UpdateProductView.as_view(),name='UpdateProduct'),
]


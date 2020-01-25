from django.shortcuts import render,HttpResponse
from django.views.generic import  View,TemplateView

# Create your views here.

class Cbview(View):
    def get(selfself,request):
        return HttpResponse("<h1>this is the CBV VIEW</h1> <a href='index/'> Index Page</a>")

class Indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['name']='Django'
        context['version']='3.0'
        return context


from django.views.generic import ListView
from .models import Brand
class BrandListview(ListView):
     context_object_name = 'brands'
     template_name = 'brand_list.html'
     model = Brand


from .models import Product
from django.views.generic import DetailView
class ProductListview(ListView):
    context_object_name = 'product_list'
    template_name = 'product_list.html'
    model=Product


class BrandDetailView(DetailView):
    context_object_name = 'brand_detail'
    model=Brand
    template_name = 'brand_detail.html'



class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'productss'
    template_name = 'product_detail.html'

from django.views.generic import CreateView

class CreateBrandView(CreateView):
    fields=('brandname','country')
    model=Brand

class CreateProductView(CreateView):
    fields=('p_name','brand','price')
    model=Product
# defaukt template name is brand_form.html


from django.views.generic import DeleteView
from django.urls import reverse_lazy
class DeleteBrandView(DeleteView):
    model=Brand
    success_url = reverse_lazy('app:Brands')

#automatically routes to the model_confirm_delete page with confrim or cancel form
#default context name for the model is modelname in lower case

from django.views.generic import UpdateView,
class UpdateProductView(UpdateView):
    model =Product
    fields=('p_name','price')


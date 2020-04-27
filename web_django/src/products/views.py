from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.core import serializers
import json


# Create your views here.
def product_create_view(request):
    print(request.GET)
    print(request.POST)
    context = {}
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)


def json_request(request):
    #obj = Product.objects.get(id=1)
    #all_products = Product.objects.all()
    all_products = serializers.serialize("json", Product.objects.all())
    #context = {
    #    'title': obj.title,
    #    'description': obj.description
    #}
    context = {
        'all_products': all_products
    }


    #json.dumps(context)
    return HttpResponse(all_products, content_type='application/json')
    #return render(request, "products/product_details.html", context)


def product_detail_view(request):
    #obj = Product.objects.get(id=1)
    #all_products = Product.objects.all()
    all_products = serializers.serialize("json", Product.objects.all())
    #context = {
    #    'title': obj.title,
    #    'description': obj.description
    #}
    context = {
        'all_products': all_products
    }
    #json.dumps(context)
    #return HttpResponse(all_products, content_type='application/json')
    return render(request, "products/product_details.html", context)


def showthis(request):

    all_objects= Product.objects.all()

    context= {'all_objects': all_objects}


    return render(request, 'products/product_details.html', context)

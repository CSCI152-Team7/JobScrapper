from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from .models import jobsInfo
# Create your views here.
def json_request_jobs(request):
    #obj = Product.objects.get(id=1)
    #all_products = Product.objects.all()
    all_jobs = serializers.serialize("json", jobsInfo.objects.all())
    #context = {
    #    'title': obj.title,
    #    'description': obj.description
    #}
    context = {
        'all_jobs': all_jobs
    }


    #json.dumps(context)
    return HttpResponse(all_jobs, content_type='application/json')
    #return render(request, "products/product_details.html", context)

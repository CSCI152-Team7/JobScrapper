"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pages.views import home_view, contact_view, about_view, search_view
from products.views import product_detail_view, product_create_view, json_request
from jobs.views import json_request_jobs

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search_view, name='jobs'),
    path('contacts/', contact_view),
    path('product/', product_detail_view),
    path('products/', json_request,name="json_request_url"),
    path('job/', product_detail_view),
    path('jobs/', json_request_jobs,name="json_request_jobs"),
    path('create/', product_create_view),
    path('abouts/', about_view),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()

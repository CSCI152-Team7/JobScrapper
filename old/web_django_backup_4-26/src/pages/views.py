from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World!! </>") #string of html code
    return render(request, "home.html", {})

def search_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contacts Page</>") #string of html code
    return render(request, "search.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contacts Page</>") #string of html code
    return render(request, "contacts.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title"   : "this is about us",
        "this_is_true" : True,
        "my_number" : 123 ,
        "my_list" : [123,321,456321,"abc"]
    }
    #return HttpResponse("<h1>Abouts Page</>") #string of html code
    return render(request, "abouts.html", my_context)

import re
from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, "singlePage/index.html")

texts = [ 
    "hello",
    "hi",
    "hola",
    "namaste",
    "halo",
]

def section(request, num):
    if num==1:
        return render(request, "add.html")
    elif num ==2:
        return render(request, "sub.html")

    else:
        raise Http404("No such section")
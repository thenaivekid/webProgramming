from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def greet(request, name):
#     return HttpResponse(f"hello, {name}!")
#http://127.0.0.1:8000/hello/ashok
#says hello to any argument passed in the url


def index(request):
    return render(request, "hello/index.html")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })

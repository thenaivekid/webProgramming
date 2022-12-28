from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "midnight/index.html",{
        "midnight":  now.hour == 00 and now.minute == 00
    })
from readline import get_endidx
from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request, title):
    if util.get_entry(title) == None:
        return HttpResponse("No page found.")
    else:
        util.get_entry(title)
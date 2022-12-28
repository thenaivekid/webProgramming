from django.shortcuts import render,redirect
from django.http import HttpResponse


from .models import VideoLink
# Create your views here.
def index(request):
    vids = VideoLink.objects.all()
    return render(request,"charisma_vids/index.html",{
        'vids':vids
    })


def add_new(request):
    if request.method != 'POST':
        return HttpResponse("Post method required")
    vid_link = request.POST['vid_link']
    vid_name = request.POST['vid_name']
    VideoLink.objects.create(link=vid_link,name=vid_name)
    return redirect('index')
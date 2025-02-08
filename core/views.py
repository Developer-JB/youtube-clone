from django.shortcuts import render
from . models import Video

# Create your views here.
def index(request):
    video = Video.objects.filter(visibility='public')
    context = {
        'video':video
    }
    return render(request, 'index.html',context)


def video_detail(request,pk):
    video=Video.objects.get(id=pk)
    context = {
        'video':video
    }
    return render(request,'video-detail.html',context)
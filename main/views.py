from django.shortcuts import render
from .models import Video, Bio, LastTrack, Galery


def index(request):
    context = {
        'title': 'Home',
        'Bio': Bio.objects.all(),
        'Video': Video.objects.all(),
        'LastTrack': LastTrack.objects.all(),
        'Galery': Galery.objects.all()
    }
    return render(request, 'main/index.html', context)

from django.shortcuts import render
from .models import Video, Bio, LastTrack, Galery


def index(request):
    galery = Galery.objects.all()
    context = {
        'title': 'Home | DJ Fankystyle',
        'Bio': Bio.objects.all(),
        'Video': Video.objects.all(),
        'LastTrack': LastTrack.objects.all(),
        'Galery': galery
    }
    return render(request, 'main/index.html', context)

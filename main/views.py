from django.shortcuts import render
from .models import Bio, LastTrack, Galery, Video


def index(request):
    galery = Galery.objects.all()
    context = {
        'title': 'Home | DJ Fankystyle',
        'Bio': Bio.objects.all(),
        'LastTrack': LastTrack.objects.all(),
        'Galery': galery,
        'Video': Video.objects.all()
    }
    return render(request, 'main/index.html', context)

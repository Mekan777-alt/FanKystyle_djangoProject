from django.shortcuts import render
from .models import Bio, LastTrack, Galery


def index(request):
    galery = Galery.objects.all()
    context = {
        'title': 'Home | DJ Fankystyle',
        'Bio': Bio.objects.all(),
        'LastTrack': LastTrack.objects.all(),
        'Galery': galery
    }
    return render(request, 'main/index.html', context)

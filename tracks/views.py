from django.shortcuts import render
from .models import Tracks, Video


def tracks(request):
    context = {
        'title': 'Tracks | Videos',
        'Tracks': Tracks.objects.all(),
        'Videos': Video.objects.all()
    }
    return render(request, 'tracks/track.html', context)

from django.shortcuts import render


def tracks(request):
    return render(request, 'tracks/track.html')

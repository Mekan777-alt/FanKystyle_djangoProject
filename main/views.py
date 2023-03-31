from django.shortcuts import render


def index(request):
    context = {
        'title': 'dj_fan',
    }
    return render(request, 'main/index.html', context)

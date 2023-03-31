from django.shortcuts import render


def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'contact/contact.html', context)

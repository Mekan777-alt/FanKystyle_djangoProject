from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    context = {
        'title': 'Contact',
        'form': ContactForm()
    }
    return render(request, 'contact/contact.html', context)


def checkout(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/index.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

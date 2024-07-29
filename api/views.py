from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import FileResponse, Http404
from django.conf import settings
import os

def about(request):
    return render(request, 'api/index.html')

def port(request):
    return render(request, 'api/portfolio.html')

def contact(request):
    return render(request, 'api/contact.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'api/success.html')
    else:
        form = ContactForm()
    return render(request, 'api/contact.html', {'form': form})



def contact_success_view(request):
    return render(request, 'api/contact_success.html')





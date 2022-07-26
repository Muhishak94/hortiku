from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        'heading': 'HORTIKU.COM',
        'subheading': 'Petani sejahtera, Negara Maju',
        'banner': 'img/logo hortiku.png',
    }
    return render(request, 'index.html', context)
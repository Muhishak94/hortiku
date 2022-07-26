from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'heading': 'MENU PANGAN',
        'subheading': 'Pangan yang tersedia langsung dari Usahatani Lokal',
        'banner': 'img/logo hortiku.png',
    }
    return render(request, 'pangan/index.html', context)
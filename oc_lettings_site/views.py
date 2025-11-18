from django.shortcuts import render


def index(request):
    """Vue principale de l'application OC Lettings Site."""
    return render(request, 'index.html')


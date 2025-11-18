"""
Vues pour l'affichage des locations.
"""
from django.shortcuts import render, get_object_or_404
from .models import Letting, Address


def index(request):
    """Vue pour afficher la liste des locations."""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Vue pour afficher le détail d'une location."""
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
"""
Vues pour l'affichage des profils utilisateurs.
"""
from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """Vue pour afficher la liste des profils."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Vue pour afficher le détail d'un profil."""
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

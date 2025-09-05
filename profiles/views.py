"""
Vues de l'application 'profiles'.

Ce module contient les vues permettant d'afficher :
    - La liste de tous les profils (index)
    - Le détail d'un profil spécifique (profile)
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """
        Vue affichant la liste de tous les profils.

        Args:
            request (HttpRequest): Objet de requête HTTP.

        Returns:
            HttpResponse: Page HTML contenant la liste des profils.

        Context:
            profiles_list (QuerySet): liste de tous les objets Profile.
        """
    # Renommé de profiles_index
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)  # Renommé de index.html


def profile(request, username):
    """
    Vue affichant le détail d'un profil spécifique.

    Args:
        request (HttpRequest): Objet de requête HTTP.
        username (str): Nom d'utilisateur associé au profil à afficher.

    Returns:
        HttpResponse: Page HTML contenant les détails du profil.

    Context:
        profile (Profile): instance du profil correspondant au username.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

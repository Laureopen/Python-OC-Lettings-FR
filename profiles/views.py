"""
Vues de l'application 'profiles'.

Ce module contient les vues permettant d'afficher :
    - La liste de tous les profils (index)
    - Le détail d'un profil spécifique (profile)
"""

import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile

# Initialisation du logger
logger = logging.getLogger(__name__)


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
    try:
        profiles_list = Profile.objects.all()
        logger.info("Liste des profils récupérée avec succès (count=%s)", profiles_list.count())
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error("Erreur lors de la récupération des profils : %s", e, exc_info=True)
        raise


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
    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info("Profil '%s' trouvé et affiché.", username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Http404:
        logger.error("Profil non trouvé pour username='%s'", username, exc_info=True)
        raise
    except Exception as e:
        logger.error("Erreur inattendue lors de l'affichage du profil '%s' : %s", username, e, exc_info=True)
        raise


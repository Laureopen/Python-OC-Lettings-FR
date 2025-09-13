"""
Vues de l'application 'lettings'.

Ce module contient les vues permettant d'afficher :
    - La liste des locations (index).
    - Le détail d'une location spécifique (letting).
"""

import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Letting

# Initialisation du logger
logger = logging.getLogger(__name__)


def index(request):
    """
    Vue d'accueil affichant la liste des locations.

    Args:
        request (HttpRequest): Objet de requête HTTP

    Returns:
        HttpResponse: Page HTML contenant la liste des locations.
    """
    try:
        lettings_list = Letting.objects.all()
        logger.info("Liste des locations récupérée avec succès (count=%s)", lettings_list.count())
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error("Erreur lors de la récupération des locations : %s", e, exc_info=True)
        raise


def letting(request, letting_id):
    """
    Vue détaillée d'une location spécifique.

    Args:
        request (HttpRequest): Objet de requête HTTP.
        letting_id (int): Identifiant unique de la location.

    Returns:
        HttpResponse: Page HTML contenant les détails de la location.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        logger.info("Location trouvée et affichée : id=%s, titre='%s'", letting_id, letting.title)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Http404:
        logger.error("Location non trouvée pour id=%s", letting_id, exc_info=True)
        raise
    except Exception as e:
        logger.error("Erreur inattendue lors de l'affichage de la location id=%s : %s", letting_id, e, exc_info=True)
        raise
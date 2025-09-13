"""
Vues principales du projet 'oc_lettings_site'.

Ce module contient la vue d'accueil générale du site.
"""
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
        Vue d'accueil générale du site.

        Args:
            request (HttpRequest): Objet de requête HTTP.

        Returns:
            HttpResponse: Page HTML de la page d'accueil du projet.
        """
    logger.info("Affiche de la vue principale par un utilisateur")
    return render(request, 'oc_lettings_site/index.html')

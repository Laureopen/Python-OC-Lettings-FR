"""
Vues principales du projet 'oc_lettings_site'.

Ce module contient la vue d'accueil générale du site.
"""
from django.shortcuts import render


# Vue d'accueil générale - reste dans l'app principale
def index(request):
    """
        Vue d'accueil générale du site.

        Args:
            request (HttpRequest): Objet de requête HTTP.

        Returns:
            HttpResponse: Page HTML de la page d'accueil du projet.
        """
    return render(request, 'oc_lettings_site/index.html')

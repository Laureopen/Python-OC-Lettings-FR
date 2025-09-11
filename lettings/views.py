"""
Vues de l'application 'lettings'.

Ce module contient les vues permettant d'afficher :
    - La liste des locations (index).
    - Le détail d'une location spécifique (letting).
"""
from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
        Vue d'accueil affichant la liste des locations.

        Args:
            request (HttpRequest): Objet de requête HTTP

        Returns:
            HttpResponse: Page HTML contenant la liste des locations.
        """

    # Renommé de lettings_index
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)  # Renommé de index.html


def letting(request, letting_id):
    """
        Vue détaillée d'une location spécifique.

        Args:
            request (HttpRequest): Objet de requête HTTP.
            letting_id (int): Identifiant unique de la location.

        Returns:
            HttpResponse: Page HTML contenant les détails de la location.
        """
    letting = get_object_or_404(Letting, id=letting_id)  # Plus sûr que .get()
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

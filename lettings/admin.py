"""
Module d'administration Django pour l'application actuelle.

Ce module enregistre les modèles Address et Letting dans l'interface
d'administration Django afin de faciliter leur gestion via l'admin site.
"""
from django.contrib import admin
from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
       Configuration de l'administration pour le modèle Address.

       Attributs :
           list_display (list) :
               Définit les champs du modèle Address qui seront affichés
               dans la liste de l'interface d'administration.
       """
    list_display = ['number', 'street', 'city', 'state', 'zip_code']


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """
        Configuration de l'administration pour le modèle Letting.

        Attributs :
            list_display (list) :
                Définit les champs du modèle Letting qui seront affichés
                dans la liste de l'interface d'administration.
        """
    list_display = ['title', 'address']

"""
Module d'administration Django pour l'application 'profiles'.

Ce module enregistre le modèle Profile dans l'interface d'administration
Django afin de faciliter sa gestion via l'admin site.
"""

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
       Configuration de l'administration pour le modèle Profile.

       Attributs :
           list_display (list) :
               Définit les champs du modèle Profile qui seront affichés
               dans la liste de l'interface d'administration.
               Ici, les champs affichés sont :
                   - user : l'utilisateur associé au profil
                   - favorite_city : la ville favorite de l'utilisateur
       """
    list_display = ['user', 'favorite_city']

"""
Configuration de l'application Django 'oc_lettings_site'.

Ce module définit la classe de configuration utilisée par Django
pour initialiser l'application principale du projet.
"""
from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
        Classe de configuration pour l'application 'oc_lettings_site'.

        Attributs :
            name (str) :
                Nom de l'application, utilisé par Django pour son enregistrement.
        """
    name = 'oc_lettings_site'

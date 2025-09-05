"""
Configuration de l'application Django 'profiles'.

Ce module définit la classe de configuration utilisée par Django
pour initialiser l'application des profils utilisateurs.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
        Classe de configuration pour l'application 'profiles'.

        Attributs :
            default_auto_field (str) :
                Définit le type de champ auto-généré par défaut pour les clés primaires.
            name (str) :
                Nom de l'application, utilisé par Django pour l'enregistrement.
        """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

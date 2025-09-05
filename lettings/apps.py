"""
Configuration de l'application Django 'lettings'.

Ce module définit la classe de configuration de l'application
qui est utilisée par Django pour l'initialisation.
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
        Classe de configuration pour l'application Lettings.

        Attributs :
            default_auto_field (str) :
                Définit le type de champ auto-généré par défaut pour les clés primaires.
            name (str) :
                Nom de l'application, utilisé par Django pour l'enregistrement.
        """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'

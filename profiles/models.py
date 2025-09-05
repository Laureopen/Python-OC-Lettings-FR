"""
Définition des modèles de l'application 'profiles'.

Ce module contient le modèle :
    - Profile : représente un profil utilisateur associé à un utilisateur Django.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
       Modèle représentant un profil utilisateur.

       Champs :
           user (OneToOneField) :
               Lien unique vers une instance de User.
           favorite_city (CharField) :
               Ville favorite de l'utilisateur, limitée à 64 caractères.
       """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """
               Métadonnées du modèle Profile.

               - verbose_name : nom singulier affiché dans l’admin.
               - verbose_name_plural : nom pluriel affiché dans l’admin.
               """
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """
                Retourne une représentation lisible du profil.

                Returns:
                    str: le nom de l'utilisateur associé au profil.
                """
        return self.user.username

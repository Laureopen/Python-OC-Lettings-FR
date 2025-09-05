"""
Définition des modèles de l'application 'lettings'.

Ce module contient les modèles :
    - Address : représente une adresse postale.
    - Letting : représente une location associée à une adresse.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
        Modèle représentant une adresse postale.

        Champs :
            number (PositiveIntegerField) :
                Numéro de rue, limité à 4 chiffres.
            street (CharField) :
                Nom de la rue, limité à 64 caractères.
            city (CharField) :
                Nom de la ville, limité à 64 caractères.
            state (CharField) :
                Code d'État à 2 lettres (ex. : 'CA', 'NY').
            zip_code (PositiveIntegerField) :
                Code postal, limité à 5 chiffres.
            country_iso_code (CharField) :
                Code ISO du pays à 3 lettres (ex. : 'USA', 'FRA').
        """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
            Métadonnées du modèle Address.

            - verbose_name : nom singulier affiché dans l’admin.
            - verbose_name_plural : nom pluriel affiché dans l’admin.
        """
        verbose_name = "address"
        verbose_name_plural = "addresses"

    def __str__(self):
        """
            Retourne une représentation lisible de l’adresse.

            Returns:
                str: numéro et rue (ex. "123 Main Street").
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
        Modèle représentant une location immobilière.

        Champs :
            title (CharField) :
                Titre de la location, limité à 256 caractères.
            address (OneToOneField) :
                Lien unique vers une instance d'Address.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """
            Métadonnées du modèle Letting.

            - verbose_name : nom singulier affiché dans l’admin.
            - verbose_name_plural : nom pluriel affiché dans l’admin.
        """
        verbose_name = "letting"
        verbose_name_plural = "lettings"

    def __str__(self):
        """
            Retourne une représentation lisible de la location.

            Returns:
                str: le titre de la location.
        """
        return self.title

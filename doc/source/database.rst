Structure de Base de Données
============================

Vue d'ensemble
--------------

L'application OC Lettings utilise SQLite avec l'ORM Django. La base de données contient deux applications principales : profiles et lettings.

Modèles de données
------------------

Application Profiles
~~~~~~~~~~~~~~~~~~~

**Modèle Profile**

.. code-block:: python

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        favorite_city = models.CharField(max_length=64, blank=True)

* **Relation 1:1** avec le modèle User de Django
* **favorite_city** : Ville favorite de l'utilisateur (optionnel)
* **Table générée** : ``Python-OC-Lettings-FR_profile``

Application Lettings
~~~~~~~~~~~~~~~~~~~

**Modèle Address**

.. code-block:: python

    class Address(models.Model):
        number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
        zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
        country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

* **number** : Numéro de rue (1-9999)
* **street** : Nom de la rue (64 caractères max)
* **city** : Ville (64 caractères max)
* **state** : État américain (2 caractères exactement)
* **zip_code** : Code postal (1-99999)
* **country_iso_code** : Code pays ISO (3 caractères exactement)
* **Table générée** : ``Python-OC-Lettings-FR_address``

**Modèle Letting**

.. code-block:: python

    class Letting(models.Model):
        title = models.CharField(max_length=256)
        address = models.OneToOneField(Address, on_delete=models.CASCADE)

* **title** : Titre de la location (256 caractères max)
* **Relation 1:1** avec Address
* **Table générée** : ``Python-OC-Lettings-FR_letting``

Schéma relationnel
-----------------

.. code-block:: text

    auth_user
        id (PK)
        ...

    Python-OC-Lettings-FR_profile
        id (PK)
        user_id (FK -> auth_user.id)
        favorite_city

    Python-OC-Lettings-FR_address
        id (PK)
        number
        street
        city
        state
        zip_code
        country_iso_code

    Python-OC-Lettings-FR_letting
        id (PK)
        title
        address_id (FK -> Python-OC-Lettings-FR_address.id)

Migrations
----------

.. code-block:: bash

    # Créer une migration
    python manage.py makemigrations

    # Appliquer les migrations
    python manage.py migrate

    # Voir l'état des migrations
    python manage.py showmigrations
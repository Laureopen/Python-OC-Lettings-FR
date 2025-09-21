Guide d'Utilisation
==================

URLs principales et fonctionnalités
-----------------------------------

Page d'accueil
~~~~~~~~~~~~~~

**URL :** http://localhost:8000

* Présentation du site Orange County Lettings
* Navigation vers les sections Profiles et Lettings

Liste des profils
~~~~~~~~~~~~~~~~~

**URL :** http://localhost:8000/profiles/

* Affichage de tous les profils utilisateurs
* Liens cliquables vers les détails de chaque profil

Détail d'un profil
~~~~~~~~~~~~~~~~~

**URL :** http://localhost:8000/profiles/<username>/

* Informations personnelles : nom d'utilisateur, email
* Ville favorite de l'utilisateur

Liste des locations
~~~~~~~~~~~~~~~~~~~

**URL :** http://localhost:8000/lettings/

* Catalogue des biens disponibles
* Titres descriptifs des propriétés

Détail d'une location
~~~~~~~~~~~~~~~~~~~~

**URL :** http://localhost:8000/lettings/<letting_id>/

* Titre de la propriété
* Adresse complète : numéro, rue, ville, état, code postal, pays

Interface d'administration
--------------------------

Accès admin
~~~~~~~~~~~

**URL :** http://localhost:8000/admin/

**Identifiants de développement :**

* Username : ``admin``
* Password : ``Abc1234!``

.. warning::
    Changez ces identifiants en production !

Sections d'administration
~~~~~~~~~~~~~~~~~~~~~~~~

* **Users** : Gestion des comptes utilisateurs
* **Profiles** : Gestion des profils et villes favorites
* **Addresses** : Gestion des adresses des biens
* **Lettings** : Gestion des locations et association avec les adresses

Cas d'utilisation typiques
--------------------------

**Visiteur :** Browse les profils et locations via l'interface publique

**Administrateur :**
* Ajoute de nouveaux biens via l'admin
* Gère les comptes utilisateurs
* Met à jour les informations des locations

**Gestionnaire immobilier :**
* Consulte l'inventaire des biens
* Vérifie les informations des propriétés
* Administre les profils clients
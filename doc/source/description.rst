Description du projet
=====================

Orange County Lettings est une start-up innovante spécialisée dans le secteur
de la **location de biens immobiliers**. Actuellement en pleine phase
d’expansion aux États-Unis. L’entreprise souhaite moderniser son site web et
renforcer son infrastructure technique pour accompagner sa croissance.


Objectifs du projet
------------------

L'application OC Lettings a pour objectifs principaux :

* **Gestion des locations** : Permettre la consultation et la gestion des biens immobiliers disponibles à la location
* **Gestion des profils** : Administrer les profils des utilisateurs de la plateforme
* **Interface intuitive** : Offrir une expérience utilisateur simple et efficace

Fonctionnalités principales
---------------------------

Gestion des locations
~~~~~~~~~~~~~~~~~~~~~

* Affichage de la liste des locations disponibles
* Consultation des détails de chaque location (adresse, numéro)
* Navigation intuitive entre les différentes propriétés

Gestion des profils
~~~~~~~~~~~~~~~~~~~

* Liste des profils utilisateurs
* Consultation des informations de profil (ville favorite, email)
* Liaison avec le système d'authentification Django

Architecture générale
--------------------

L'application suit une architecture Django classique :

* **Modèle MVT** (Model-View-Template) de Django
* **Base de données SQLite** pour le stockage des données
* **Templates HTML** avec CSS pour l'interface utilisateur
* **Système d'authentification** Django intégré
* **Panel d'administration** automatisé

Instructions d'Installation
===========================

Prérequis système
-----------------

Avant d'installer le projet, assurez-vous d'avoir les éléments suivants :

Logiciels requis
~~~~~~~~~~~~~~~~

* **Python 3.6 ou supérieur** - Interpréteur Python
* **Git** - Système de contrôle de version
* **SQLite3** - Base de données (généralement inclus avec Python)
* **Pip** - Gestionnaire de paquets Python (inclus avec Python)

Comptes nécessaires
~~~~~~~~~~~~~~~~~~~

* **Compte GitHub** avec accès en lecture au repository
* **Accès Internet** pour le téléchargement des dépendances

Vérification des prérequis
~~~~~~~~~~~~~~~~~~~~~~~~~

Vérifiez que Python est installé correctement :

.. code-block:: bash

    python --version
    # ou
    python3 --version

Vérifiez que Git est installé :

.. code-block:: bash

    git --version

Installation du projet
---------------------

Étape 1 : Clonage du repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/put/project/in
    git clone https://github.com/Laureopen/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

Étape 2 : Création de l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Sur Linux/macOS :**

.. code-block:: bash

    python -m venv venv

**Sur Ubuntu (si erreur de paquet) :**

.. code-block:: bash

    apt-get install python3-venv

**Sur Windows :**

.. code-block:: powershell

    python -m venv venv

Étape 3 : Activation de l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Sur Linux/macOS :**

.. code-block:: bash

    source venv/bin/activate

**Sur Windows (PowerShell) :**

.. code-block:: powershell

    .\venv\Scripts\Activate.ps1

**Sur Windows (CMD) :**

.. code-block:: cmd

    venv\Scripts\activate

Étape 4 : Vérification de l'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vérifiez que Python pointe vers l'environnement virtuel :

**Sur Linux/macOS :**

.. code-block:: bash

    which python
    which pip

**Sur Windows :**

.. code-block:: powershell

    (Get-Command python).Path
    (Get-Command pip).Path

Vérifiez la version de Python :

.. code-block:: bash

    python --version

Étape 5 : Installation des dépendances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install --requirement requirements.txt

Cette commande installe toutes les dépendances nécessaires listées dans le fichier ``requirements.txt``.

Configuration de la base de données
-----------------------------------

Le projet utilise SQLite par défaut. La base de données sera automatiquement créée lors du premier lancement.

Migrations de base de données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si nécessaire, appliquez les migrations :

.. code-block:: bash

    python manage.py migrate

Création d'un super utilisateur (optionnel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour accéder à l'interface d'administration :

.. code-block:: bash

    python manage.py createsuperuser

Désactivation de l'environnement virtuel
----------------------------------------

Lorsque vous avez terminé de travailler sur le projet :

.. code-block:: bash

    deactivate

Dépannage
---------

Problèmes courants
~~~~~~~~~~~~~~~~~

**Erreur de permissions sur Linux/macOS :**

.. code-block:: bash

    sudo apt-get install python3-venv  # Ubuntu/Debian
    # ou
    brew install python3              # macOS avec Homebrew

**Module non trouvé :**

Vérifiez que l'environnement virtuel est activé et que les dépendances sont installées :

.. code-block:: bash

    pip list
    pip install --requirement requirements.txt

**Problèmes de base de données :**

Supprimez la base de données existante et recréez-la :

.. code-block:: bash

    rm oc-lettings-site.sqlite3  # Attention : supprime les données !
    python manage.py migrate

Installation avec Docker (Alternative)
--------------------------------------

Si vous préférez utiliser Docker, le projet peut également être lancé avec Docker Compose :

Lancement avec Docker
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Construction des images Docker
    docker-compose build

    # Lancement des conteneurs
    docker-compose up

L'application sera alors accessible sur http://localhost:8000

Notes importantes
-----------------

* Gardez toujours l'environnement virtuel activé lors du développement
* Le fichier ``requirements.txt`` contient toutes les versions exactes des dépendances
* La base de données SQLite sera créée dans le répertoire racine du projet
* Sauvegardez régulièrement vos données si vous utilisez l'application en production
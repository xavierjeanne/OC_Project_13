Installation
============

Prérequis
---------

* Python 3.13 ou supérieur
* pip (gestionnaire de paquets Python)
* Git

Installation locale
-------------------

1. Cloner le repository
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/xavierjeanne/OC_Project_13.git
   cd OC_Project_13

2. Créer un environnement virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate

3. Installer les dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   pip install -r requirements.txt

4. Configurer les variables d'environnement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Créer un fichier ``.env`` à la racine du projet :

.. code-block:: text

   SECRET_KEY=votre-clé-secrète-django
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=votre-dsn-sentry (optionnel)

5. Appliquer les migrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python manage.py migrate

6. Charger les données de test (optionnel)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python load_fixtures.py

7. Lancer le serveur de développement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python manage.py runserver

L'application sera accessible à l'adresse http://localhost:8000

Installation avec Docker
------------------------

1. Construire l'image Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker build -t oc-lettings .

2. Lancer le conteneur
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker run -p 8000:8000 \
     -e SECRET_KEY=votre-clé \
     -e DEBUG=False \
     oc-lettings

3. Utiliser Docker Compose
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker-compose up

Configuration pour le développement
------------------------------------

Interface d'administration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Pour accéder à l'interface d'administration Django :

1. Créer un superutilisateur :

   .. code-block:: bash

      python manage.py createsuperuser

2. Accéder à http://localhost:8000/admin

Tests
^^^^^

Pour exécuter les tests :

.. code-block:: bash

   # Tous les tests
   pytest
   
   # Avec couverture
   pytest --cov
   
   # Rapport HTML de couverture
   pytest --cov --cov-report=html

Linting
^^^^^^^

Pour vérifier la qualité du code :

.. code-block:: bash

   flake8

Collecte des fichiers statiques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python manage.py collectstatic

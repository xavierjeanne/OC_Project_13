Référence API
=============

Cette section documente les modules, classes et fonctions de l'application OC Lettings.

Application Lettings
--------------------

Models
^^^^^^

.. automodule:: lettings.models
   :members:
   :undoc-members:
   :show-inheritance:

Views
^^^^^

.. automodule:: lettings.views
   :members:
   :undoc-members:
   :show-inheritance:

Admin
^^^^^

.. automodule:: lettings.admin
   :members:
   :undoc-members:
   :show-inheritance:

URLs
^^^^

.. automodule:: lettings.urls
   :members:
   :undoc-members:
   :show-inheritance:

Application Profiles
--------------------

Models
^^^^^^

.. automodule:: profiles.models
   :members:
   :undoc-members:
   :show-inheritance:

Views
^^^^^

.. automodule:: profiles.views
   :members:
   :undoc-members:
   :show-inheritance:

Admin
^^^^^

.. automodule:: profiles.admin
   :members:
   :undoc-members:
   :show-inheritance:

URLs
^^^^

.. automodule:: profiles.urls
   :members:
   :undoc-members:
   :show-inheritance:

Application principale (oc_lettings_site)
------------------------------------------

Settings
^^^^^^^^

.. automodule:: oc_lettings_site.settings
   :members:
   :undoc-members:

Views
^^^^^

.. automodule:: oc_lettings_site.views
   :members:
   :undoc-members:
   :show-inheritance:

URLs
^^^^

.. automodule:: oc_lettings_site.urls
   :members:
   :undoc-members:

Scripts utilitaires
-------------------

Load Fixtures
^^^^^^^^^^^^^

.. automodule:: load_fixtures
   :members:
   :undoc-members:
   :show-inheritance:

Architecture
------------

Structure du projet
^^^^^^^^^^^^^^^^^^^

::

   OC_Project_13/
   ├── lettings/               # Application des locations
   │   ├── migrations/         # Migrations de base de données
   │   ├── templates/          # Templates spécifiques
   │   ├── tests/              # Tests unitaires
   │   ├── models.py           # Modèles Address et Letting
   │   ├── views.py            # Vues de l'application
   │   ├── urls.py             # Configuration des URLs
   │   └── admin.py            # Configuration admin
   ├── profiles/               # Application des profils
   │   ├── migrations/         # Migrations de base de données
   │   ├── templates/          # Templates spécifiques
   │   ├── tests/              # Tests unitaires
   │   ├── models.py           # Modèle Profile
   │   ├── views.py            # Vues de l'application
   │   ├── urls.py             # Configuration des URLs
   │   └── admin.py            # Configuration admin
   ├── oc_lettings_site/       # Application principale
   │   ├── settings.py         # Configuration Django
   │   ├── urls.py             # URLs racine
   │   ├── views.py            # Vue d'accueil
   │   └── wsgi.py             # Point d'entrée WSGI
   ├── templates/              # Templates partagés
   │   ├── base.html           # Template de base
   │   ├── index.html          # Page d'accueil
   │   ├── 404.html            # Page erreur 404
   │   └── 500.html            # Page erreur 500
   ├── static/                 # Fichiers statiques source
   ├── staticfiles/            # Fichiers statiques collectés
   ├── doc/                    # Documentation Sphinx
   ├── .github/workflows/      # CI/CD GitHub Actions
   ├── Dockerfile              # Configuration Docker
   ├── docker-compose.yml      # Docker Compose
   ├── requirements.txt        # Dépendances Python
   ├── pytest.ini              # Configuration pytest
   ├── setup.cfg               # Configuration flake8
   └── manage.py               # CLI Django

Modèle de données
^^^^^^^^^^^^^^^^^

.. code-block:: text

   ┌─────────────────┐
   │     Address     │
   ├─────────────────┤
   │ id (PK)         │
   │ number          │
   │ street          │
   │ city            │
   │ state           │
   │ zip_code        │
   │ country_iso_code│
   └─────────────────┘
           ▲
           │
           │ 1:1
           │
   ┌─────────────────┐
   │    Letting      │
   ├─────────────────┤
   │ id (PK)         │
   │ title           │
   │ address_id (FK) │
   └─────────────────┘


   ┌─────────────────┐
   │      User       │
   │   (Django)      │
   ├─────────────────┤
   │ id (PK)         │
   │ username        │
   │ email           │
   │ first_name      │
   │ last_name       │
   └─────────────────┘
           ▲
           │
           │ 1:1
           │
   ┌─────────────────┐
   │    Profile      │
   ├─────────────────┤
   │ id (PK)         │
   │ user_id (FK)    │
   │ favorite_city   │
   └─────────────────┘

Documentation OC Lettings
=========================

Bienvenue dans la documentation de **OC Lettings**, une application web Django moderne 
pour la gestion de locations immobilières et de profils utilisateurs.

.. image:: https://img.shields.io/badge/Python-3.13-blue.svg
   :target: https://www.python.org/
   :alt: Python 3.13

.. image:: https://img.shields.io/badge/Django-4.2-green.svg
   :target: https://www.djangoproject.com/
   :alt: Django 4.2

.. image:: https://img.shields.io/badge/Docker-Ready-blue.svg
   :target: https://www.docker.com/
   :alt: Docker Ready

Présentation
------------

OC Lettings est une application web développée avec Django qui permet de :

* 📍 Gérer des locations immobilières avec leurs adresses
* 👤 Gérer des profils utilisateurs avec leurs informations
* 🔐 Interface d'administration complète
* 🐳 Déploiement via Docker et CI/CD
* 📊 Monitoring des erreurs avec Sentry
* 🎨 Interface utilisateur moderne et responsive

Caractéristiques principales
-----------------------------

* **Architecture modulaire** : Applications Django séparées (lettings, profiles)
* **Tests complets** : Couverture de code >80% avec pytest
* **CI/CD automatisé** : Pipeline GitHub Actions pour tests, build et déploiement
* **Containerisé** : Dockerfile et docker-compose pour déploiement facile
* **Monitoring** : Intégration Sentry pour suivi des erreurs en production
* **Documentation** : Documentation complète avec Sphinx et Read the Docs

Démarrage rapide
----------------

.. code-block:: bash

   # Cloner le projet
   git clone https://github.com/xavierjeanne/OC_Project_13.git
   cd OC_Project_13

   # Installer les dépendances
   pip install -r requirements.txt

   # Lancer le serveur
   python manage.py migrate
   python manage.py runserver

Visitez http://localhost:8000 pour voir l'application.

Table des matières
------------------

.. toctree::
   :maxdepth: 2
   :caption: Guide utilisateur

   installation
   usage

.. toctree::
   :maxdepth: 2
   :caption: Documentation technique

   api
   deployment

Liens utiles
------------

* `Repository GitHub <https://github.com/xavierjeanne/OC_Project_13>`_
* `Documentation Read the Docs <https://oc-lettings.readthedocs.io>`_
* `Pipeline CI/CD <https://github.com/xavierjeanne/OC_Project_13/actions>`_

Support
-------

Pour toute question ou problème, veuillez :

* Consulter la section :doc:`deployment` pour le dépannage
* Ouvrir une issue sur GitHub
* Consulter les logs Sentry pour les erreurs en production

Licence
-------

Ce projet est développé dans le cadre d'un projet pédagogique OpenClassrooms.

Indices et tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


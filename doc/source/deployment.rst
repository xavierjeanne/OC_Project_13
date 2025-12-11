Déploiement
===========

Cette section explique comment déployer l'application OC Lettings en production.

Vue d'ensemble
--------------

Le déploiement utilise un pipeline CI/CD automatisé via GitHub Actions :

1. **Tests** : Exécution de flake8 et pytest
2. **Build** : Construction de l'image Docker
3. **Push** : Envoi de l'image vers Docker Hub
4. **Deploy** : Déploiement automatique sur Render

Prérequis
---------

Comptes requis
^^^^^^^^^^^^^^

* Compte GitHub (repository du projet)
* Compte Docker Hub (pour stocker les images)
* Compte Sentry (monitoring des erreurs)
* Compte Render ou autre hébergeur (pour le déploiement)

Secrets GitHub à configurer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans les paramètres du repository GitHub (Settings > Secrets and variables > Actions) :

* ``DOCKER_USERNAME`` : Nom d'utilisateur Docker Hub
* ``DOCKER_PASSWORD`` : Token d'accès Docker Hub
* ``SENTRY_DSN`` : URL du projet Sentry

Configuration Docker Hub
------------------------

1. Créer un compte sur https://hub.docker.com
2. Créer un repository (ex: ``username/oc-lettings``)
3. Générer un Access Token :

   * Account Settings > Security > New Access Token
   * Donner un nom descriptif
   * Copier le token généré

4. Ajouter les secrets dans GitHub

Configuration Sentry
--------------------

1. Créer un compte sur https://sentry.io
2. Créer un nouveau projet Django
3. Copier le DSN fourni (format : ``https://xxx@xxx.ingest.sentry.io/xxx``)
4. Ajouter ``SENTRY_DSN`` dans les secrets GitHub

Pipeline CI/CD
--------------

Le fichier ``.github/workflows/ci-cd.yml`` définit trois jobs :

Job 1 : Tests
^^^^^^^^^^^^^

Exécuté sur **toutes les branches** lors d'un push ou pull request :

* Installation de Python 3.13
* Installation des dépendances
* Vérification flake8
* Exécution des tests avec pytest
* Vérification de la couverture (>80%)

Job 2 : Build & Push
^^^^^^^^^^^^^^^^^^^^

Exécuté **uniquement sur master** après succès des tests :

* Build de l'image Docker
* Tag avec le hash du commit
* Push vers Docker Hub avec deux tags :

  * ``latest``
  * ``master-<commit-hash>``

Job 3 : Deploy
^^^^^^^^^^^^^^

Exécuté après succès du build :

* Notification du déploiement
* Déclenchement du redéploiement sur Render

Déploiement sur Render
-----------------------

Configuration initiale
^^^^^^^^^^^^^^^^^^^^^^

1. Créer un compte sur https://render.com
2. Connecter le repository GitHub
3. Créer un nouveau Web Service
4. Sélectionner :

   * **Environment** : Docker
   * **Branch** : master
   * **Region** : Frankfurt (EU) ou Oregon (US)

5. Configurer les variables d'environnement :

   * ``SECRET_KEY`` : Clé secrète Django unique
   * ``DEBUG`` : ``False``
   * ``ALLOWED_HOSTS`` : ``.onrender.com``
   * ``SENTRY_DSN`` : URL Sentry

Génération de SECRET_KEY
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Mise à jour de ALLOWED_HOSTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Après le premier déploiement, mettre à jour avec l'URL exacte :

.. code-block:: text

   nom-du-service.onrender.com,.onrender.com

Déploiement automatique
^^^^^^^^^^^^^^^^^^^^^^^^

Une fois configuré :

1. Chaque push sur ``master`` déclenche le pipeline
2. Si les tests passent, l'image Docker est buildée
3. L'image est poussée sur Docker Hub
4. Render détecte la mise à jour et redéploie automatiquement

Vérification du déploiement
----------------------------

Après déploiement, vérifier :

* ✅ Site accessible via l'URL Render
* ✅ Fichiers statiques (CSS/JS) chargés
* ✅ Navigation fonctionnelle
* ✅ Interface admin accessible
* ✅ Erreurs remontées dans Sentry

Tests de l'image Docker
------------------------

Extraire et tester localement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Pull l'image depuis Docker Hub
   docker pull username/oc-lettings:latest
   
   # Lancer le conteneur
   docker run -p 8000:8000 \
     -e SECRET_KEY=test-key \
     -e DEBUG=False \
     -e ALLOWED_HOSTS=localhost \
     username/oc-lettings:latest
   
   # Accéder à http://localhost:8000

Maintenance
-----------

Mise à jour des dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   pip list --outdated
   pip install --upgrade package-name
   pip freeze > requirements.txt

Surveillance Sentry
^^^^^^^^^^^^^^^^^^^

1. Se connecter au dashboard Sentry
2. Consulter les erreurs remontées
3. Analyser les stack traces
4. Corriger les bugs identifiés

Rollback en cas d'erreur
^^^^^^^^^^^^^^^^^^^^^^^^^

Si un déploiement échoue :

1. Dans Render, aller dans l'historique des déploiements
2. Sélectionner un déploiement précédent fonctionnel
3. Cliquer sur "Redeploy"

Ou en local avec Docker :

.. code-block:: bash

   docker pull username/oc-lettings:master-<ancien-hash>
   docker run -p 8000:8000 username/oc-lettings:master-<ancien-hash>

Monitoring
----------

Logs Render
^^^^^^^^^^^

Accessible dans le dashboard Render :

* Logs en temps réel
* Historique des builds
* Métriques de performance (CPU, RAM)

Dashboard Sentry
^^^^^^^^^^^^^^^^

* Nombre d'erreurs par jour
* Types d'erreurs les plus fréquentes
* Utilisateurs affectés
* Stack traces détaillées

Bonnes pratiques
----------------

* ✅ Toujours tester localement avant de push
* ✅ Vérifier que les tests passent sur la branche
* ✅ Ne jamais commiter de secrets dans le code
* ✅ Utiliser des variables d'environnement
* ✅ Consulter Sentry régulièrement
* ✅ Documenter les changements importants
* ✅ Faire des commits atomiques et descriptifs

Dépannage
---------

Build Docker échoue
^^^^^^^^^^^^^^^^^^^^

* Vérifier que ``requirements.txt`` est à jour
* Vérifier la syntaxe du ``Dockerfile``
* Tester le build localement : ``docker build -t test .``

Tests échouent sur GitHub Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Exécuter les tests localement : ``pytest``
* Vérifier les dépendances dans ``requirements.txt``
* Consulter les logs détaillés dans GitHub Actions

Site inaccessible après déploiement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Vérifier les variables d'environnement sur Render
* Consulter les logs Render
* Vérifier ``ALLOWED_HOSTS``
* S'assurer que ``SECRET_KEY`` est défini

Fichiers statiques ne chargent pas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Vérifier que WhiteNoise est installé
* Vérifier la configuration dans ``settings.py``
* Exécuter ``collectstatic`` manuellement
* Consulter les logs pour erreurs 404

Guide d'utilisation
===================

Accueil
-------

La page d'accueil de l'application OC Lettings présente :

* Un lien vers la liste des locations (Lettings)
* Un lien vers la liste des profils utilisateurs (Profiles)

Gestion des locations
----------------------

Liste des locations
^^^^^^^^^^^^^^^^^^^

Accessible via ``/lettings/``, cette page affiche :

* Le titre de chaque location
* Un lien cliquable vers les détails de la location

Détails d'une location
^^^^^^^^^^^^^^^^^^^^^^

Accessible via ``/lettings/<id>/``, cette page affiche :

* Le titre de la location
* L'adresse complète :
  
  * Numéro et rue
  * Ville, État, Code postal
  * Code pays ISO

Gestion des profils
--------------------

Liste des profils
^^^^^^^^^^^^^^^^^

Accessible via ``/profiles/``, cette page affiche :

* Le nom d'utilisateur de chaque profil
* Un lien cliquable vers les détails du profil

Détails d'un profil
^^^^^^^^^^^^^^^^^^^

Accessible via ``/profiles/<username>/``, cette page affiche :

* Prénom et nom de l'utilisateur
* Email
* Ville favorite

Interface d'administration
--------------------------

L'interface d'administration Django permet de :

* Gérer les utilisateurs et leurs permissions
* Créer, modifier et supprimer des adresses
* Créer, modifier et supprimer des locations
* Gérer les profils utilisateurs

Accès à l'administration
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Aller sur ``/admin/``
2. Se connecter avec un compte superutilisateur
3. Accéder aux différents modules :

   * **Lettings** : Adresses et Locations
   * **Profiles** : Profils utilisateurs
   * **Auth** : Utilisateurs et groupes

Ajouter une location
^^^^^^^^^^^^^^^^^^^^

1. Dans l'administration, aller dans **Lettings** > **Addresses**
2. Cliquer sur **Ajouter Address**
3. Remplir les champs requis :

   * Number
   * Street
   * City
   * State (2 lettres)
   * Zip code
   * Country ISO code (3 lettres)

4. Sauvegarder
5. Aller dans **Lettings** > **Lettings**
6. Cliquer sur **Ajouter Letting**
7. Choisir un titre et l'adresse créée
8. Sauvegarder

Ajouter un profil
^^^^^^^^^^^^^^^^^

1. Créer d'abord un utilisateur dans **Auth** > **Users**
2. Aller dans **Profiles** > **Profiles**
3. Cliquer sur **Ajouter Profile**
4. Sélectionner l'utilisateur et entrer la ville favorite
5. Sauvegarder

Gestion des erreurs
-------------------

Pages d'erreur personnalisées
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'application gère les erreurs avec des pages personnalisées :

* **404** : Page non trouvée
* **500** : Erreur serveur interne

Ces pages maintiennent le style de l'application et offrent :

* Un message explicatif
* Un lien de retour à l'accueil

Monitoring avec Sentry
^^^^^^^^^^^^^^^^^^^^^^

Les erreurs en production sont automatiquement envoyées à Sentry pour :

* Suivi en temps réel
* Stack traces détaillées
* Alertes par email
* Statistiques d'erreurs

API REST (Future)
-----------------

Note : L'application actuelle n'expose pas d'API REST.
La documentation sera mise à jour lors de l'ajout de cette fonctionnalité.

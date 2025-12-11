# 📚 Configuration Read the Docs

## Vue d'ensemble

Ce guide explique comment configurer et publier la documentation sur Read the Docs.

## Étape 1 : Créer un compte Read the Docs

1. Aller sur https://readthedocs.org
2. Cliquer sur **"Sign Up"**
3. Choisir **"Sign up with GitHub"** (recommandé)
4. Autoriser Read the Docs à accéder à votre compte GitHub

## Étape 2 : Importer le projet

### 2.1 Depuis le dashboard

1. Une fois connecté, cliquer sur **"Import a Project"**
2. Cliquer sur le bouton **"+"** à côté de **"Import a Repository"**
3. Sélectionner **"Connect to GitHub"**

### 2.2 Autoriser l'accès

1. Dans la popup GitHub, autoriser Read the Docs
2. Vous pouvez autoriser tous les repos ou seulement certains
3. Sélectionner **OC_Project_13** dans la liste

### 2.3 Configuration du projet

Read the Docs détectera automatiquement :

- ✅ Le fichier `.readthedocs.yaml` à la racine
- ✅ La documentation Sphinx dans `doc/`
- ✅ Le fichier `requirements.txt` pour les dépendances

Paramètres par défaut :
```
Name: oc-project-13
Repository: https://github.com/xavierjeanne/OC_Project_13
Default branch: master
Documentation type: Sphinx HTML
```

## Étape 3 : Configuration avancée

### 3.1 Build automatique

Par défaut, Read the Docs build automatiquement à chaque push sur master.

Pour configurer :

1. Aller dans **Admin** > **Advanced Settings**
2. Vérifier que **"Build on commit"** est activé
3. Sélectionner les branches à documenter (master, develop, etc.)

### 3.2 Versions

Read the Docs crée automatiquement des versions pour :

- ✅ **latest** : Dernière version de master
- ✅ **stable** : Dernière release taguée
- ✅ Toutes les branches actives

Pour gérer les versions :

1. Aller dans **Versions**
2. Activer/désactiver les versions à documenter
3. Définir la version par défaut (généralement "stable" ou "latest")

### 3.3 Variables d'environnement

Si votre documentation nécessite des variables d'environnement :

1. Aller dans **Admin** > **Environment Variables**
2. Ajouter les variables nécessaires (ex: `DJANGO_SETTINGS_MODULE`)

**Note :** Pour ce projet, les variables sont déjà configurées dans `doc/source/conf.py`

## Étape 4 : Lancer le premier build

### 4.1 Build manuel

1. Aller dans **Builds**
2. Cliquer sur **"Build Version: latest"**
3. Observer les logs en temps réel

### 4.2 Vérifier le build

Le build doit :
- ✅ Installer Python 3.13
- ✅ Installer les dépendances depuis `requirements.txt`
- ✅ Exécuter Sphinx
- ✅ Générer HTML, PDF et ePub

### 4.3 Résoudre les erreurs

Si le build échoue :

1. Consulter les logs détaillés
2. Vérifier que `requirements.txt` contient Sphinx
3. Vérifier la configuration dans `.readthedocs.yaml`
4. Tester localement : `python -m sphinx -b html doc/source doc/build/html`

## Étape 5 : Accéder à la documentation

### 5.1 URL de la documentation

Une fois le build réussi, la documentation sera accessible à :

```
https://oc-project-13.readthedocs.io/en/latest/
```

Ou avec votre nom d'utilisateur :
```
https://<votre-nom>.readthedocs.io/<project-name>/
```

### 5.2 Badge pour le README

Ajouter un badge dans votre README.md :

```markdown
[![Documentation Status](https://readthedocs.org/projects/oc-project-13/badge/?version=latest)](https://oc-project-13.readthedocs.io/en/latest/?badge=latest)
```

## Étape 6 : Webhooks GitHub

### 6.1 Vérification automatique

Read the Docs configure automatiquement un webhook sur votre repository GitHub.

Pour vérifier :

1. Aller sur GitHub : **Settings** > **Webhooks**
2. Vous devriez voir un webhook pour `readthedocs.org`
3. Vérifier que le statut est vert (✓)

### 6.2 Test du webhook

1. Faire une modification dans `doc/source/index.rst`
2. Commit et push vers master
3. Aller sur Read the Docs > **Builds**
4. Observer le nouveau build automatique

## Étape 7 : Personnalisation

### 7.1 Domaine personnalisé

Pour utiliser un domaine personnalisé :

1. Aller dans **Admin** > **Domains**
2. Ajouter votre domaine (ex: `docs.monsite.com`)
3. Configurer un CNAME DNS pointant vers `readthedocs.io`

### 7.2 Thème personnalisé

Le projet utilise déjà `sphinx_rtd_theme` (Read the Docs Theme).

Pour personnaliser davantage :

1. Éditer `doc/source/conf.py`
2. Modifier `html_theme_options` :
   ```python
   html_theme_options = {
       'logo_only': False,
       'display_version': True,
       'prev_next_buttons_location': 'bottom',
       'style_external_links': True,
       'navigation_depth': 4,
   }
   ```

### 7.3 Formats de sortie

Par défaut, Read the Docs génère :
- ✅ HTML
- ✅ PDF
- ✅ ePub

Pour désactiver certains formats :

1. Éditer `.readthedocs.yaml`
2. Modifier la section `formats` :
   ```yaml
   formats:
     - pdf  # Seulement PDF
   ```

## Checklist finale

- [ ] Compte Read the Docs créé
- [ ] Projet importé depuis GitHub
- [ ] Premier build réussi
- [ ] Documentation accessible en ligne
- [ ] Webhook GitHub configuré
- [ ] Badge ajouté au README
- [ ] Build automatique testé (push → rebuild)
- [ ] Versions configurées correctement

## Liens utiles

| Resource | URL |
|----------|-----|
| Dashboard Read the Docs | https://readthedocs.org/dashboard/ |
| Documentation projet | https://oc-project-13.readthedocs.io |
| Builds | https://readthedocs.org/projects/oc-project-13/builds/ |
| Guide officiel | https://docs.readthedocs.io/en/stable/ |

## Dépannage

### Build échoue avec "Module not found"

**Solution :** Ajouter le module manquant dans `requirements.txt`

```bash
pip freeze | grep <module-name>
# Ajouter dans requirements.txt
```

### Documentation ne se met pas à jour

**Solutions :**
1. Vérifier le webhook GitHub (doit être actif)
2. Forcer un rebuild manuel depuis Read the Docs
3. Vérifier les logs de build pour erreurs

### Erreur "Configuration file not found"

**Solution :** Vérifier que `.readthedocs.yaml` est à la racine du projet

```bash
git add .readthedocs.yaml
git commit -m "Add Read the Docs configuration"
git push
```

### Thème ne s'affiche pas correctement

**Solution :** Vérifier l'installation de `sphinx-rtd-theme`

```python
# Dans doc/source/conf.py
html_theme = 'sphinx_rtd_theme'

# Dans requirements.txt
sphinx-rtd-theme>=2.0.0
```

---

*Guide créé le 11 décembre 2025 - Configuration Read the Docs pour OC Lettings*

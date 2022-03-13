[![CircleCI](https://circleci.com/gh/RafaRemote/P13_oc_lettings_site_redone/tree/main.svg?style=svg)](https://circleci.com/gh/RafaRemote/scale_a_django_app/tree/main)


## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest --reuse-db --no-migrations`


#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell: `sqlite3`
- Se connecter à la base de données: `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données: `.tables`
- Afficher les colonnes dans le tableau des profils: `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils: `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter (ou CONTROL-D)

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Pour le déploiement: 

Nous utilisons un Pipeline CircleCi.



Le workflow comprend un élément nommé `deploy-application`, il comprend les `jobs` suivants:

- test-linting:
  - vérifie la conformité PEP8,
- python/test:
  - si job précédent a réussi: effectue les tests décrits dans le code
- build-and-push:
  - si job précédent a réussi: 
    - build image docker,
    - push image sur docker hub.
- heroky-deploy:
  - si job précédent a réussi:
    - déploiement du site sur Heroku.

Lien pour le Pipeline CircleCi: 

https://app.circleci.com/pipelines/github/RafaRemote/scale_a_django_app?branch=main  

Lien pour le site déployé sur Heroku:  

https://ocletting7.herokuapp.com/  

Pour accéder au monitoring Sentry vous devez avoir un compte Sentry, donc si ce n'est pas déjà fait, créer un compte Sentry.  

https://sentry.io/signup/  

Une fois que vous avez votre compte: utilisez le lien ci-dessous:  

https://sentry.io/organizations/raphael-vu/issues/?project=6244042  

Et cliquez sur `Request to join`.  

L'administrateur du projet devra vous autoriser à rejoindre ce projet, vous recevrez un mail vous indiquant cet accord.  


Pour utiliser une image Docker, vous devez avoir Docker installer sur votre machine, si ce n'est pas fait, suivez le lien suivant:  

https://docs.docker.com/get-docker/  

Pour utiliser une image Docker, suivez la procédure suivante:  

Dans votre terminal, assurez vous d'avoir Docker installé sur votre machine en tapant `docker --version`, sinon installer docker avec la commande `pip install docker` (doc: https://docker-py.readthedocs.io/en/stable/).  


Suivez ce lien vers le repository Docker Hub pour les images Docker:  

https://hub.docker.com/repository/docker/rafaremote/oc_lettings  

Pour télécharger le dernier build de l'application, choisissez la dernière image du repo oc_lettings. Pour cela cliquer sur le premier tag de la liste à apparaître et relever le tag entier, qui devrait ressembler à quelque-chose comme ceci:  

`rafaremote/oc_lettings:a503562237cc423a0827f05537b896c5677a8929`  

Enfin dans votre terminal, taper la commande suivante:  

`docker run -it -p 8000:8000` suivi d'un espace et du tag  
# README

## Description(FR)

Bienvenue dans l'Application de Gestion de Chambre de Croissance pour la Culture de Champignons ! Cette application a été conçue pour simplifier et optimiser le processus de gestion des sacs de champignons dans la chambre de croissance, en éliminant le chaos et les pertes de temps liés à la recherche d'emplacements spécifiques.

## Fonctionnalités

- **Ensemencement Facilité** : Lorsqu'un lot est ensemencé, l'opérateur entre simplement le nombre de sacs, et l'application lui indique instantanément les emplacements appropriés dans la chambre de croissance.

- **Gestion Optimisée** : Après deux semaines, l'application propose de manière automatisée les sacs à déplacer en salle de fructification, en précisant également leur emplacement.

- **Gain de Temps** : Cette application a été développée en début de stage et a été améliorée grâce aux retours de l'employeur. Elle permet de gagner un temps précieux en évitant les recherches fastidieuses et les erreurs humaines.

## Installation

Pour installer et exécuter l'application, suivez ces étapes :

1. Clonez le référentiel sur votre machine locale.
2. Assurez-vous d'avoir Python installé.
3. Accédez au répertoire de l'application.
4. Exécutez la commande suivante pour démarrer l'application :

## Description (EN)

Welcome to the Mushroom Growth Chamber Management Application! This application has been designed to simplify and optimize the process of managing mushroom bags in the growth chamber, eliminating chaos and time losses associated with searching for specific locations.

## Features

- **Easy Seeding**: When a batch is seeded, the operator simply enters the number of bags, and the application instantly provides the appropriate locations in the growth chamber.

- **Optimized Management**: After two weeks, the application automatically suggests the bags to be moved to the fruiting room, specifying their location.

- **Time Savings**: This application was developed at the beginning of the internship and has been improved based on feedback from the employer. It saves valuable time by avoiding tedious searches and human errors.

## Installation

To install and run the application, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the application directory.
4. Run the following command to start the application:


## Tester et compiler sur Windows

### Tester sur sa machine dans un environnement virtuel Python

Sur Windows, ouvrir une fenêtre Powershell à la racine du projet (si la commande `python` ne fonctionne pas, réinstaller python en cochant l'option "AJOUTER AU PATH" lors de l'installation) :
- Installer le module virtualenv : `pip install virtualenv`
- Créer un environnement virtuel python (nommé `win_env`, plus d'info sur [ce lien](https://virtualenv.pypa.io/en/latest/user_guide.html)) : `virtualenv win_env`
- Se placer dans cet environnement virtuel : `.\win_env\Scripts\activate.ps1`
- Une fois placé dans l'environnement virtuel, (win_env) devrait apparaître devant chaque ligne. Installez alors les dépendances dans cet environnement virtuel : `pip install -r requirements.txt`
- Lancer l'application en exécutant le script appli.py : `python appli.py`

### Compiler l'application dans un fichier exe :

Toujours dans l'environnement virtuel (voir partie précédente), il faut commencer par installer le module `pyinstaller` avec la commande `pip install pyinstaller`. Pour comprendre ce que fait ce module et comment l'utiliser, voir [la documentation](https://pyinstaller.org/en/stable/index.html).

On peut exécuter la commande suivante pour compiler le projet en un fichier .exe à retrouver dans le dossier `dist`. Pour débugger, on peut compiler le projet dans un dossier plutôt qu'un fichier en enlevant l'option `--onefile`. Voir plus d'information sur la commande et ses options sur [ce lien](https://pyinstaller.org/en/v5.13.0/usage.html).

```powershell
pyinstaller.exe `
    --name appli_windows `
    -y --windowed --clean --onefile `
    --paths .\win_env\Lib\site-packages\ `
    --add-data "assets;assets" `
    appli.py
```

## Tester et compiler sur Linux

Installer Tkinter avec le gestionnaire de paquet.

- Sur Arch : `sudo pacman -S tk`
- Sur Ubuntu/Debian : `sudo apt install tk`

Créer l'environnement virtuel, installer les dépendances et installer `pyinstaller` avec pip dans l'environnement virtuel également.

Pour compiler, depuis la racine du projet, utiliser la commande suivante : 

```bash
pyinstaller \
    --name appli_linux \
    -y --windowed --clean --onefile \
    --paths lin_env/lib/python3.11/site-packages \
    --add-data "assets:assets" \
    --hidden-import='PIL._tkinter_finder' \ 
    appli.py
```
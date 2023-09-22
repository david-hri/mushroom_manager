# README

## Changements apportés à l'application par Téo

- Réorganisation des fichiers : désormais, les scripts python sont à la racine du projets et tous les fichiers nécessaires au bon fonctionnement de l'application sont dans le dossier `assets`. Les chemins vers les fichiers dans les scripts ont été modifié en conséquence.
- Vérification du système d'exploitation pendant l'exécution du programme car l'utilisation de fichier .ico n'est pas supporté sur Linux et fait planter le programme (voir `appli.py` ligne 90)
- Vérification de la manière dont le programme est exécuté (avec python ou dans un .exe) pour résoudre les problèmes de lecture des fichiers dans le dossier `assets` (voir variable `folder` dans `fonctions_principales.py` qui est ensuite importée et utilisée dans les deux autres scripts à chaque fois qu'on a spécifie le chemin d'un fichier dans `assets`).
- Rédaction de cette documentation et génération d'un fichier `requirements.txt` pour fixer les versions des dépendances du projet (à regénérer à chaque fois qu'un nouveau module est installé dans l'environnement virtuel avec la commande `pip freeze > requirements.txt` exécutée elle aussi dans l'environnement virtuel).

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
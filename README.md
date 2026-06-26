# TaskFlow

## Présentation

TaskFlow est une application de gestion de tâches développée en Python.

Elle fonctionne dans le terminal et permet de gérer des tâches :
ajouter une tâche, afficher les tâches, terminer une tâche et supprimer une tâche.

Ce projet a été réalisé pendant le stage Altikva afin de pratiquer Python, Git et GitHub.

## Objectif du projet

L'objectif de TaskFlow est de pratiquer le développement d'une application Python complète.

Le projet permet de travailler l'organisation du code, la gestion des données, l'utilisation de Git et GitHub ainsi que les bonnes pratiques de développement.

## Fonctionnalités

L'application permet de :

- ajouter une tâche
- afficher toutes les tâches
- terminer une tâche
- supprimer une tâche
- définir une priorité entre 1 et 5
- ajouter une date d'échéance
- valider les entrées utilisateur
- sauvegarder les tâches dans une base SQLite
- utiliser des commandes dans le terminal avec argparse

## Organisation du projet

Le projet est organisé avec plusieurs dossiers :

src/

-main.py : lancement de l'application

-cli.py : interface utilisateur avec argparse

-storage.py : gestion de la sauvegarde SQLite

-models.py : modèle d'une tâche avec dataclass


tests/

- contient les tests du projet


README.md :

- explique le fonctionnement du projet


.gitignore :

- permet d'ignorer certains fichiers dans Git


taskflow.db :

- contient la base locale SQLite


## Technologies utilisées

- Python 3
- Git
- GitHub
- SQLite
- argparse
- dataclasses
- datetime
- Visual Studio Code


## Installation

Cloner le projet :

git clone https://github.com/sadioondoua/TaskFlow.git


Entrer dans le dossier :

cd TaskFlow


Créer un environnement virtuel :

python -m venv venv


Activer l'environnement virtuel :

venv\Scripts\activate


## Utilisation de pip

Pour voir les paquets installés :

pip list


Pour installer un paquet :

pip install nom_du_paquet


## Lancement du programme

Depuis le dossier du projet :

python src/main.py


## Commandes disponibles

Ajouter une tâche :

python src/main.py add "Ma tâche"


Ajouter une tâche avec une priorité :

python src/main.py add "Réviser Python" --priority 3


Ajouter une tâche avec priorité et échéance :

python src/main.py add "Projet SQLite" --priority 2 --due-date 2026-07-01


Afficher les tâches :

python src/main.py list


Terminer une tâche :

python src/main.py done 0


Supprimer une tâche :

python src/main.py remove 0


## Sauvegarde des données

Les tâches sont enregistrées automatiquement dans une base locale SQLite :

taskflow.db


Cela permet de retrouver les tâches après avoir fermé le programme.

La sauvegarde utilise SQLite avec les opérations :

- création
- lecture
- modification
- suppression


## Validation des données

Les données saisies sont vérifiées avant l'enregistrement.

La priorité doit être comprise entre 1 et 5.

Les dates d'échéance doivent respecter le format :

AAAA-MM-JJ


Le module datetime est utilisé pour vérifier les dates.


## Git utilisé

J'ai utilisé Git pour gérer les versions du projet.


Création d'une branche de travail :

git checkout -b feature/semaine3


Ajouter les modifications :

git add .


Créer un commit :

git commit -m "feat: ajout fonctionnalité"


Envoyer la branche vers GitHub :

git push origin feature/semaine3


Revenir sur la branche principale :

git checkout main


Fusionner la branche feature avec main :

git merge feature/semaine3


Envoyer la version finale :

git push origin main


Version du projet :

v0.2


Cette version correspond à la migration du stockage JSON vers SQLite.


## Auteur

Arnauld Sadio Ondoua

Stage Altikva - 2026
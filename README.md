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
- supprimer une tâche avec une confirmation
- sauvegarder les tâches dans un fichier JSON

## Organisation du projet

Le projet est organisé avec plusieurs dossiers :

src/
- main.py : lance le programme
- todo.py : contient les fonctions de gestion des tâches

tests/
- contient les tests du projet

README.md :
- explique le fonctionnement du projet

.gitignore :
- permet d'ignorer certains fichiers dans Git

tasks.json :
- contient les tâches sauvegardées


## Technologies utilisées

- Python 3
- Git
- GitHub
- JSON
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

Le projet utilise principalement les bibliothèques déjà disponibles avec Python.


## Lancement du programme

Depuis le dossier du projet :

python src/main.py


## Sauvegarde des données

Les tâches sont enregistrées automatiquement dans le fichier :

tasks.json

Cela permet de retrouver les tâches après avoir fermé le programme.


## Git utilisé

J'ai utilisé Git pour gérer les versions du projet.

Création d'une branche de travail :

git checkout -b feature/semaine1

Ajouter les modifications :

git add .

Créer un commit :

git commit -m "feat: ajout fonctionnalité"

Envoyer la branche vers GitHub :

git push origin feature/semaine1

Revenir sur la branche principale :

git checkout main

Fusionner la branche feature avec main :

git merge feature/semaine1

Envoyer la version finale :

git push origin main


## Auteur

Arnauld Sadio Ondoua

Stage Altikva - 2026


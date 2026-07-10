# TaskFlow



![Python CI](https://github.com/sadioondoua/TaskFlow/actions/workflows/python-test.yml/badge.svg)

## Présentation

TaskFlow est une application de gestion de tâches développée en Python.

Elle fonctionne en ligne de commande et permet de gérer des tâches :
ajouter une tâche, afficher les tâches, terminer une tâche et supprimer une tâche.

Ce projet a été réalisé pendant le stage Altikva afin de pratiquer Python, Git et GitHub.

## Objectif du projet

L'objectif de TaskFlow est de pratiquer le développement d'une application Python complète.

Le projet permet de travailler l'organisation du code, la gestion des données avec SQLite, l'écriture de tests automatisés et la mise en place d'une intégration continue avec GitHub Actions.

## Fonctionnalités

L'application permet de :

* ajouter une tâche
* afficher toutes les tâches
* terminer une tâche
* supprimer une tâche
* définir une priorité entre 1 et 5
* ajouter une date d'échéance
* valider les entrées utilisateur
* sauvegarder les tâches dans une base SQLite
* utiliser des commandes dans le terminal avec argparse

## Organisation du projet

Le projet est organisé avec plusieurs dossiers :

src/

* main.py : lancement de l'application
* cli.py : interface utilisateur avec argparse
* storage.py : gestion de la base SQLite (CRUD)
* models.py : modèle d'une tâche avec dataclass

tests/

* test\_todo.py : contient les tests automatisés avec pytest

.github/

* workflows/python-test.yml : exécution automatique des tests avec GitHub Actions

README.md :

* documentation du projet

.gitignore :

* permet d'ignorer les fichiers qui ne doivent pas être envoyés sur GitHub

taskflow.db :

* contient la base de données SQLite

requirements.txt :

* contient les dépendances du projet

## Technologies utilisées

* Python 3
* Git
* GitHub
* SQLite
* argparse
* dataclasses
* datetime
* pytest
* Ruff
* GitHub Actions
* Visual Studio Code

## Installation

Cloner le projet :

git clone https://github.com/sadioondoua/TaskFlow.git

Entrer dans le dossier :

cd TaskFlow

Créer un environnement virtuel :

python -m venv venv

Activer l'environnement virtuel :

venv\\Scripts\\activate

Installer les dépendances :

pip install -r requirements.txt

## Utilisation de pip

Pour voir les paquets installés :

pip list

Pour installer les dépendances du projet :

pip install -r requirements.txt

## Lancement du programme

Depuis le dossier du projet :

python src/main.py

## Commandes disponibles

Ajouter une tâche :

python src/main.py add "Ma tâche"

Ajouter une tâche avec une priorité :

python src/main.py add "Réviser Python" --priority 3

Ajouter une tâche avec une priorité et une échéance :

python src/main.py add "Projet SQLite" --priority 2 --due-date 2026-07-01

Afficher les tâches :

python src/main.py list

Terminer une tâche :

python src/main.py done 1

Supprimer une tâche :

python src/main.py remove 1

## Sauvegarde des données

Les tâches sont enregistrées automatiquement dans une base de données SQLite.

Les opérations suivantes sont prises en charge :

* création
* lecture
* modification
* suppression

## Validation des données

Les données saisies sont vérifiées avant leur enregistrement.

* la priorité doit être comprise entre 1 et 5
* la date doit respecter le format AAAA-MM-JJ
* le titre d'une tâche ne peut pas être vide

## Tests

Le projet utilise pytest pour vérifier le bon fonctionnement des principales fonctionnalités.

Pour lancer les tests :

pytest -v

Les tests couvrent notamment :

* l'ajout d'une tâche
* l'affichage des tâches
* la modification du statut d'une tâche
* la suppression d'une tâche
* le stockage des données

## Qualité du code

Le projet utilise Ruff pour vérifier la qualité et le style du code.

Vérifier le code :

ruff check .

Formater le code :

ruff format .

## Intégration continue

Le projet utilise GitHub Actions.

À chaque push sur GitHub, un workflow est exécuté automatiquement afin de :

* installer les dépendances
* vérifier le code avec Ruff
* lancer les tests pytest

Cela permet de vérifier que le projet reste fonctionnel après chaque modification.

## Git utilisé

J'ai utilisé Git pour gérer les différentes versions du projet.

Création d'une branche :

git checkout -b feature/semaine4

Ajouter les modifications :

git add .

Créer un commit :

git commit -m "feat: ajout des tests et de la CI"

Envoyer la branche :

git push origin feature/semaine4

Fusionner avec la branche principale :

git checkout main

git merge feature/semaine4

Envoyer la version finale :

git push origin main

## Version du projet

v0.3

Cette version ajoute les tests automatisés avec pytest, la vérification du code avec Ruff et l'intégration continue avec GitHub Actions.

## Auteur

Arnauld Sadio Ondoua

Stage Altikva - 2026


# TaskFlow

## Présentation

TaskFlow est une application de gestion de tâches développée en Python.

Elle fonctionne dans le terminal et permet de gérer des tâches :
ajouter une tâche, afficher les tâches, terminer une tâche et supprimer une tâche.

Ce projet a été réalisé pendant le stage Altikva afin de pratiquer Python, Git, GitHub, la structuration d'un projet et la gestion des données.

## Objectif du projet

L'objectif de TaskFlow est de pratiquer le développement d'une application Python complète avec une organisation propre du code.

Le projet permet de travailler :

* les fonctions Python
* les modules
* les dataclasses
* la gestion des erreurs
* SQLite
* Git et GitHub
* les bonnes pratiques de développement

## Fonctionnalités

L'application permet de :

* ajouter une tâche
* afficher toutes les tâches
* terminer une tâche
* supprimer une tâche
* définir une priorité entre 1 et 5
* ajouter une date d'échéance
* valider les entrées utilisateur
* sauvegarder les données dans une base SQLite
* utiliser une interface en ligne de commande avec argparse

## Organisation du projet

Le projet est organisé avec plusieurs dossiers :

src/

* main.py : lancement de l'application

* cli.py : interface en ligne de commande avec argparse

* todo.py : logique métier des tâches

* storage.py : gestion de la sauvegarde SQLite (création, lecture, modification, suppression)

* models.py : modèle Task avec dataclass

tests/

* contient les tests du projet

README.md :

* explique le fonctionnement du projet

.gitignore :

* contient les fichiers ignorés par Git

taskflow.db :

* base locale SQLite contenant les tâches

## Technologies utilisées

* Python 3
* SQLite
* Git
* GitHub
* Visual Studio Code

## Installation

Cloner le projet :

```bash
git clone https://github.com/sadioondoua/TaskFlow.git
```

Entrer dans le dossier :

```bash
cd TaskFlow
```

Créer un environnement virtuel :

```bash
python -m venv venv
```

Activer l'environnement virtuel :

```bash
venv\Scripts\activate
```

## Utilisation de pip

Voir les paquets installés :

```bash
pip list
```

Installer un paquet :

```bash
pip install nom_du_paquet
```

## Lancement du programme

Depuis le dossier du projet :

```bash
python src/main.py
```

## Commandes disponibles

Ajouter une tâche :

```bash
python src/main.py add "Ma tâche"
```

Ajouter une tâche avec priorité :

```bash
python src/main.py add "Réviser Python" --priority 3
```

Ajouter une tâche avec une échéance :

```bash
python src/main.py add "Projet" --priority 2 --due-date 2026-07-01
```

Afficher les tâches :

```bash
python src/main.py list
```

Terminer une tâche :

```bash
python src/main.py done 1
```

Supprimer une tâche :

```bash
python src/main.py remove 1
```

## Sauvegarde des données

Les tâches sont enregistrées automatiquement dans une base locale SQLite :

```
taskflow.db
```

SQLite permet de conserver les données après fermeture du programme et de gérer les opérations de création, lecture, modification et suppression.

## Git utilisé

J'ai utilisé Git pour gérer les versions du projet.

Création d'une branche :

```bash
git checkout -b feature/semaine3
```

Ajouter les modifications :

```bash
git add .
```

Créer un commit :

```bash
git commit -m "feat: ajout validation priorité et échéance des tâches"
```

Envoyer la branche vers GitHub :

```bash
git push origin feature/semaine3
```

Fusionner avec main :

```bash
git checkout main
git merge feature/semaine3
```

## Ce sur quoi j'ai galéré

Les principales difficultés rencontrées ont été :

* comprendre la séparation entre les différents modules Python
* passer d'une sauvegarde JSON à une base SQLite
* comprendre le fonctionnement de Git avec les branches et les commits
* gérer les erreurs de saisie utilisateur
* organiser le code pour qu'il soit plus facile à maintenir

## Auteur

Arnauld Sadio Ondoua

Stage Altikva - 2026



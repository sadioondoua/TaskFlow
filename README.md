# TaskFlow

## Présentation

TaskFlow est une application de gestion de tâches développée en Python.

Elle fonctionne en ligne de commande et permet de :
- ajouter une tâche
- afficher les tâches
- terminer une tâche
- supprimer une tâche

Le projet a été réalisé pendant le stage Altikva afin de pratiquer Python, Git, GitHub, la structuration d'un projet et la gestion des données.

## Objectif du projet

L'objectif de TaskFlow est de créer une application Python propre et organisée.

Le projet permet de travailler :
- les fonctions Python
- les modules
- les dataclasses
- la gestion des erreurs
- SQLite
- argparse
- Git et GitHub

## Fonctionnalités

L'application permet de :

- ajouter une tâche
- afficher toutes les tâches
- terminer une tâche
- supprimer une tâche
- définir une priorité entre 1 et 5
- ajouter une date d'échéance
- vérifier les erreurs de saisie
- sauvegarder les données dans une base SQLite
- utiliser une interface en ligne de commande avec argparse

## Organisation du projet

```text
src/

main.py
    Lancement de l'application

cli.py
    Interface en ligne de commande avec argparse

models.py
    Modèle Task avec dataclass

storage.py
    Gestion de la base SQLite
    (création, lecture, modification, suppression)

tests/

test_todo.py
    Tests des fonctionnalités principales
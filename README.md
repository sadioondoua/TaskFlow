# TaskFlow

## Présentation

TaskFlow est une application de gestion de tâches en ligne de commande développée en Python.

Elle permet à un utilisateur de créer, afficher, terminer et supprimer des tâches directement depuis le terminal.

Ce projet a été réalisé dans le cadre du stage Altikva afin de mettre en pratique les bases du développement Python, l'utilisation de Git et GitHub ainsi que la structuration d'un projet.

---

## Objectifs Python utilisés

Ce projet permet de pratiquer plusieurs notions fondamentales de Python :

- Variables
- Listes
- Fonctions
- Conditions
- Boucles
- Lecture et écriture de fichiers JSON
- Organisation du code en plusieurs fichiers

---

## Fonctionnalités

L'application permet de :

- Ajouter une tâche
- Afficher toutes les tâches
- Marquer une tâche comme terminée
- Supprimer une tâche avec confirmation
- Sauvegarder automatiquement les données dans un fichier JSON

---

## Structure du projet

```
TaskFlow/

├── src/
│   ├── main.py
│   └── todo.py
│
├── tests/
│
├── screenshots/
│
├── README.md
│
├── .gitignore
│
├── tasks.json
│
└── venv/
```

---

## Technologies utilisées

- Python 3
- Git
- GitHub
- JSON
- Visual Studio Code

---

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/sadioondoua/taskflow.git
```

Entrer dans le dossier du projet :

```bash
cd taskflow
```

Créer l'environnement virtuel :

```bash
python -m venv venv
```

Activer l'environnement virtuel sous Windows :

```bash
venv\Scripts\activate
```

---

## Utilisation de pip

Vérifier les paquets installés dans l'environnement virtuel :

```bash
pip list
```

Le projet utilise uniquement des modules intégrés à Python.
Aucune dépendance externe n'est nécessaire.

---

## Lancement de l'application

Depuis la racine du projet :

```bash
python src/main.py
```

---

## Sauvegarde des données

Les tâches sont sauvegardées automatiquement dans le fichier :

```
tasks.json
```

Cela permet de conserver les tâches même après la fermeture du programme.

---

## Git

Le projet utilise Git pour suivre les modifications du code.

Commandes principales utilisées :

```bash
git add
git commit
git push
```

Le développement a été réalisé avec une branche feature puis fusionné dans la branche principale.

---

## Auteur

Arnauld Sadio Ondoua

Stage Altikva - 2026
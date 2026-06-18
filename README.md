# TaskFlow

## Présentation

TaskFlow est une application de gestion de tâches en ligne de commande développée en Python.

Elle permet à un utilisateur d'ajouter, afficher, terminer et supprimer des tâches directement depuis le terminal.

Ce projet a été réalisé dans le cadre du stage Altikva afin de mettre en pratique les fondamentaux de Python, Git et GitHub, ainsi que les bonnes pratiques de structuration d'un projet logiciel.

---

## Objectifs pédagogiques

Ce projet permet de travailler les notions suivantes :

* Variables
* Listes
* Fonctions
* Conditions
* Boucles
* Lecture et écriture de fichiers JSON
* Refactorisation du code
* Utilisation de Git et GitHub
* Gestion des branches Git
* Utilisation d'un environnement virtuel Python (venv)

---

## Fonctionnalités

L'application permet de :

* Ajouter une tâche
* Lister les tâches
* Marquer une tâche comme terminée
* Supprimer une tâche avec confirmation
* Sauvegarder automatiquement les données dans un fichier JSON

---

## Structure du projet

```text
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

* Python 3
* Git
* GitHub
* JSON
* Visual Studio Code

---

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/sadioondoua/TaskFlow.git
```

Entrer dans le dossier du projet :

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

---

## Utilisation de pip

Vérifier les paquets installés :

```bash
pip list
```

Le projet utilise uniquement les bibliothèques standards de Python.

---

## Lancement de l'application

Depuis la racine du projet :

```bash
python src/main.py
```

---

## Sauvegarde des données

Les tâches sont sauvegardées dans :

```text
tasks.json
```

Les données restent disponibles même après la fermeture du programme.

---

## Workflow Git utilisé

Création d'une branche de travail :

```bash
git checkout -b feature/semaine1
```

Ajout des modifications :

```bash
git add .
```

Création d'un commit :

```bash
git commit -m "feat: nouvelle fonctionnalité"
```

Envoi vers GitHub :

```bash
git push origin feature/semaine1
```

Fusion dans la branche principale :

```bash
git checkout main
git merge feature/semaine1
```

---

## Auteur

Arnauld Sadio Ondoua

Stage Altikva – 2026

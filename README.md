# TaskFlow

![Python CI](https://github.com/sadioondoua/TaskFlow/actions/workflows/python-test.yml/badge.svg)

## Présentation

TaskFlow est une application de gestion de tâches développée en Python.

Elle fonctionne en ligne de commande et permet de gérer des tâches :
- ajouter une tâche ;
- afficher les tâches ;
- terminer une tâche ;
- supprimer une tâche.

Au fil du stage, le projet a évolué pour intégrer une base de données SQLite, une API REST avec FastAPI, des tests automatisés, une intégration continue avec GitHub Actions, un système de journalisation (logging), un export CSV ainsi que le packaging Python.

Ce projet a été réalisé pendant le stage ALTIKVA afin de pratiquer Python, Git, GitHub et les bonnes pratiques de développement logiciel.

---

## Objectif du projet

L'objectif de TaskFlow est de pratiquer le développement d'une application Python complète.

Le projet permet de travailler l'organisation du code, la gestion des données avec SQLite, l'écriture de tests automatisés, la mise en place d'une intégration continue avec GitHub Actions, la création d'une API REST et la distribution d'un package Python.

---

## Fonctionnalités

L'application permet de :

- ajouter une tâche ;
- afficher toutes les tâches ;
- terminer une tâche ;
- supprimer une tâche ;
- définir une priorité entre 1 et 5 ;
- ajouter une date d'échéance ;
- valider les entrées utilisateur ;
- sauvegarder les tâches dans une base SQLite ;
- utiliser des commandes dans le terminal avec argparse ;
- exporter les tâches au format CSV ;
- afficher des statistiques sur les tâches ;
- accéder aux tâches via une API REST FastAPI ;
- enregistrer automatiquement certaines actions grâce au système de logging.

---

## Organisation du projet

Le projet est organisé avec plusieurs dossiers :

### src/

- main.py : lancement de l'application
- cli.py : interface utilisateur avec argparse
- storage.py : gestion de la base SQLite (CRUD)
- models.py : modèle d'une tâche avec dataclass
- api.py : gestion des jours fériés
- web_api.py : API REST FastAPI
- export.py : export des tâches au format CSV
- analyse.py : statistiques sur les tâches
- logging_config.py : configuration du système de journalisation (logging)

### tests/

- test_todo.py : contient les tests automatisés avec pytest

### .github/

- workflows/python-test.yml : exécution automatique des tests avec GitHub Actions

### README.md

- documentation du projet

### .gitignore

- permet d'ignorer les fichiers qui ne doivent pas être envoyés sur GitHub

### taskflow.db

- contient la base de données SQLite

### requirements.txt

- contient les dépendances du projet

### pyproject.toml

- configuration du package Python

### config.ini

- contient les paramètres de configuration de l'application

### dist/

- contient les packages Python générés (.whl et .tar.gz)

### build/

- contient les fichiers générés lors du packaging.

---

## Technologies utilisées

- Python 3
- Git
- GitHub
- SQLite
- argparse
- dataclasses
- datetime
- pytest
- Ruff
- GitHub Actions
- Visual Studio Code
- FastAPI
- Uvicorn
- logging
- build
- wheel
- twine
- pyproject.toml
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

Sous Windows :

```bash
venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Utilisation de pip

Pour voir les paquets installés :

```bash
pip list
```

Pour installer les dépendances du projet :

```bash
pip install -r requirements.txt
```

---

## Lancement du programme

Depuis le dossier du projet :

```bash
python src/main.py
```

---

## Commandes disponibles

Ajouter une tâche :

```bash
python src/main.py add "Ma tâche"
```

Ajouter une tâche avec une priorité :

```bash
python src/main.py add "Réviser Python" --priority 3
```

Ajouter une tâche avec une priorité et une échéance :

```bash
python src/main.py add "Projet SQLite" --priority 2 --due-date 2026-07-01
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

Afficher les statistiques :

```bash
python src/main.py stats
```

Exporter les tâches :

```bash
python src/main.py export
```

---

## Sauvegarde des données

Les tâches sont enregistrées automatiquement dans une base de données SQLite.

Les opérations suivantes sont prises en charge :

- création ;
- lecture ;
- modification ;
- suppression.

---

## Validation des données

Les données saisies sont vérifiées avant leur enregistrement.

- la priorité doit être comprise entre 1 et 5 ;
- la date doit respecter le format AAAA-MM-JJ ;
- le titre d'une tâche ne peut pas être vide.

---

## Tests

Le projet utilise pytest pour vérifier le bon fonctionnement des principales fonctionnalités.

Pour lancer les tests :

```bash
pytest -v
```

Les tests couvrent notamment :

- l'ajout d'une tâche ;
- l'affichage des tâches ;
- la modification du statut d'une tâche ;
- la suppression d'une tâche ;
- le stockage des données.

---

## Qualité du code

Le projet utilise Ruff pour vérifier la qualité et le style du code.

Vérifier le code :

```bash
ruff check .
```

Formater le code :

```bash
ruff format .
```

---

## Intégration continue

Le projet utilise GitHub Actions.

À chaque push sur GitHub, un workflow est exécuté automatiquement afin de :

- installer les dépendances ;
- vérifier le code avec Ruff ;
- lancer les tests pytest.

Cela permet de vérifier que le projet reste fonctionnel après chaque modification.

---

## Git utilisé

J'ai utilisé Git pour gérer les différentes versions du projet.

Création d'une branche :

```bash
git checkout -b feature/semaine4
```

Ajouter les modifications :

```bash
git add .
```

Créer un commit :

```bash
git commit -m "feat: ajout des tests et de la CI"
```

Envoyer la branche :

```bash
git push origin feature/semaine4
```

Fusionner avec la branche principale :

```bash
git checkout main
git merge feature/semaine4
git push origin main
```

---

## Version du projet

**v1.0**

Cette version finale comprend :

- l'application TaskFlow complète ;
- SQLite ;
- FastAPI ;
- les tests automatisés avec pytest ;
- Ruff ;
- GitHub Actions ;
- l'export CSV ;
- les statistiques ;
- le système de logging ;
- le packaging Python ;
- la génération des fichiers `.whl` et `.tar.gz`.

---

# 🌐 API FastAPI

L'application TaskFlow possède également une interface Web développée avec FastAPI.

## Lancer l'API

```bash
python -m uvicorn src.web_api:app --reload
```

L'API est disponible à l'adresse :

```
http://127.0.0.1:8000
```

Documentation Swagger :

```
http://127.0.0.1:8000/docs
```

---

## Routes disponibles

### GET /tasks

Retourne toutes les tâches.

```bash
curl http://127.0.0.1:8000/tasks
```

### POST /tasks

Ajoute une nouvelle tâche.

```json
{
  "title": "Apprendre FastAPI",
  "priority": 2,
  "due_date": "2026-07-30",
  "done": false,
  "holiday": false
}
```

### PATCH /tasks/{id}/done

Marque une tâche comme terminée.

```bash
curl -X PATCH http://127.0.0.1:8000/tasks/195/done
```

---

## Packaging Python

Le projet peut être distribué sous la forme d'un package Python.

Construire le package :

```bash
python -m build
```

Vérifier le package :

```bash
twine check dist/*
```

Publier le package :

```bash
twine upload --repository testpypi dist/*
```

---

## Journalisation (Logging)

Le projet utilise le module **logging** de Python.

Les principales actions enregistrées sont :

- ajout d'une tâche ;
- suppression d'une tâche ;
- validation d'une tâche.

Cette fonctionnalité facilite le suivi de l'utilisation de l'application.

---

## Difficultés rencontrées

Au cours du développement, plusieurs difficultés ont été rencontrées :

- prise en main de Git et GitHub ;
- découverte de SQLite ;
- compréhension de pytest ;
- configuration de GitHub Actions ;
- création de l'API FastAPI ;
- packaging Python et publication sur TestPyPI.

Ces difficultés m'ont permis de mieux comprendre le développement d'une application Python complète.

---

## Compétences acquises

Grâce à ce projet, j'ai appris à :

- développer une application Python organisée ;
- manipuler SQLite ;
- créer une API REST avec FastAPI ;
- utiliser Git et GitHub efficacement ;
- écrire des tests automatisés ;
- utiliser GitHub Actions ;
- créer un package Python installable ;
- documenter un projet logiciel.

---

## Améliorations possibles

Les évolutions suivantes pourraient être ajoutées :

- interface graphique ;
- authentification des utilisateurs ;
- notifications avant les échéances ;
- synchronisation avec une base de données distante ;
- export PDF ;
- déploiement de l'API sur Internet.

---

## Auteur

Arnauld Sadio Ondoua

Projet réalisé durant le stage de 8 semaines chez **ALTIKVA** en 2026.

---

## Licence

Projet pédagogique réalisé dans le cadre du stage ALTIKVA.

Utilisation libre à des fins d'apprentissage.
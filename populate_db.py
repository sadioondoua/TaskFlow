import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from models import Task
from storage import add_task

tasks = [
    ("Réviser Python", 1, "2026-07-10"),
    ("Préparer réunion", 2, "2026-07-11"),
    ("Lire documentation API", 3, "2026-07-12"),
    ("Faire les tests", 4, "2026-07-13"),
    ("Corriger bugs", 5, "2026-07-14"),
    ("Créer README", 2, "2026-07-15"),
    ("Mettre à jour GitHub", 3, "2026-07-16"),
    ("Nettoyer le code", 1, "2026-07-17"),
    ("Préparer présentation", 4, "2026-07-18"),
    ("Étudier pandas", 5, "2026-07-19"),
    ("Découvrir requests", 2, "2026-07-20"),
    ("Faire export CSV", 3, "2026-07-21"),
    ("Créer statistiques", 1, "2026-07-22"),
    ("Tester API", 4, "2026-07-23"),
    ("Documenter le projet", 2, "2026-07-24"),
    ("Relire le code", 3, "2026-07-25"),
    ("Préparer démonstration", 5, "2026-07-26"),
    ("Vérifier Git", 1, "2026-07-27"),
    ("Fusionner branche", 2, "2026-07-28"),
    ("Livrer le projet", 3, "2026-07-29"),
]

for title, priority, due_date in tasks:
    add_task(
        Task(
            title=title,
            priority=priority,
            due_date=due_date,
            done=False,
            holiday=False,
        )
    )

print("20 tâches ajoutées avec succès.")

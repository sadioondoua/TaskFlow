import sqlite3
from pathlib import Path

from models import Task


DATABASE = Path(__file__).resolve().parent.parent / "taskflow.db"


def create_table() -> None:
    """
    Crée la table tasks si elle n'existe pas.
    """

    try:
        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                priority INTEGER NOT NULL,
                due_date TEXT,
                done BOOLEAN NOT NULL,
                holiday BOOLEAN NOT NULL
            )
            """
        )

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        print(f"Erreur SQLite : {error}")


def add_task(task: Task) -> None:
    """
    Ajoute une tâche dans la base SQLite.
    """

    try:
        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO tasks(title, priority, due_date, done, holiday)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                task.title,
                task.priority,
                task.due_date,
                task.done,
                task.holiday,
            ),
        )

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        print(f"Erreur SQLite : {error}")


def get_tasks() -> list[Task]:
    """
    Retourne toutes les tâches enregistrées.
    """

    try:
        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM tasks")

        rows = cursor.fetchall()

        connection.close()

        return [
            Task(
                id=row[0],
                title=row[1],
                priority=row[2],
                due_date=row[3],
                done=bool(row[4]),
                holiday=bool(row[5]),
            )
            for row in rows
        ]

    except sqlite3.Error as error:
        print(f"Erreur SQLite : {error}")

        return []


def update_task(task_id: int, done: bool) -> bool:
    """
    Modifie le statut d'une tâche.

    Retourne True si une tâche existe et est modifiée.
    """

    try:
        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET done = ?
            WHERE id = ?
            """,
            (done, task_id),
        )

        connection.commit()

        modified = cursor.rowcount

        connection.close()

        return modified > 0

    except sqlite3.Error as error:
        print(f"Erreur SQLite : {error}")

        return False


def delete_task(task_id: int) -> bool:
    """
    Supprime une tâche.

    Retourne True si une tâche a été supprimée.
    """

    try:
        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )

        connection.commit()

        deleted = cursor.rowcount

        connection.close()

        return deleted > 0

    except sqlite3.Error as error:
        print(f"Erreur SQLite : {error}")

        return False


def clear_tasks() -> None:
    """
    Supprime toutes les tâches de la base.
    """

    try:
        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        cursor.execute("DELETE FROM tasks")

        connection.commit()

        connection.close()

    except sqlite3.Error as error:
        print(f"Erreur SQLite : {error}")

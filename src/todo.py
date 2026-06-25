from models import Task
from storage import (
    create_table,
    add_task as save_task,
    get_tasks,
    update_task,
    delete_task
)


create_table()


def create_new_task(title: str, priority: int, due_date: str | None = None) -> None:
    """
    Crée une nouvelle tâche.
    """

    if not title.strip():
        print("Erreur : le titre ne peut pas être vide")
        return

    task = Task(
        id=0,
        title=title,
        priority=priority,
        due_date=due_date
    )

    save_task(task)

    print("Tâche ajoutée avec succès")


def list_tasks() -> None:
    """
    Affiche les tâches.
    """

    tasks = get_tasks()

    if not tasks:
        print("La liste des tâches est vide")
        return

    for task in tasks:
        status = "✅" if task.done else "❌"

        print(
            f"{task.id} - {status} {task.title} "
            f"(priorité {task.priority})"
        )


def complete_task(task_id: int) -> None:
    """
    Termine une tâche.
    """

    update_task(task_id, True)

    print("Tâche terminée ✅")


def remove_task(task_id: int) -> None:
    """
    Supprime une tâche.
    """

    delete_task(task_id)

    print("Tâche supprimée ✅")
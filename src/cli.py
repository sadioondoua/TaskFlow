import argparse
from datetime import datetime

from models import Task
from storage import (
    add_task,
    get_tasks,
    update_task,
    delete_task
)


def validate_priority(priority: int) -> None:
    """
    Vérifie que la priorité est comprise entre 1 et 5.
    """

    if priority < 1 or priority > 5:
        raise ValueError(
            "La priorité doit être comprise entre 1 et 5"
        )


def validate_due_date(due_date: str | None) -> None:
    """
    Vérifie le format de la date d'échéance.
    """

    if due_date is not None:

        try:
            datetime.strptime(
                due_date,
                "%Y-%m-%d"
            )

        except ValueError:
            raise ValueError(
                "La date doit être au format AAAA-MM-JJ"
            )


def create_new_task(
    title: str,
    priority: int,
    due_date: str | None = None
) -> None:
    """
    Crée une nouvelle tâche.
    """

    if not title.strip():
        print("Erreur : le titre ne peut pas être vide")
        return

    try:
        validate_priority(priority)
        validate_due_date(due_date)

    except ValueError as error:
        print(f"Erreur : {error}")
        return


    task = Task(
        id=0,
        title=title,
        priority=priority,
        due_date=due_date
    )


    add_task(task)

    print("Tâche ajoutée avec succès")


def list_tasks() -> None:
    """
    Affiche toutes les tâches.
    """

    tasks = get_tasks()


    if not tasks:
        print("La liste des tâches est vide")
        return


    for task in tasks:

        status = "✅" if task.done else "❌"

        print(
            f"{task.id} - {status} {task.title} "
            f"(priorité {task.priority}) "
            f"(échéance : {task.due_date})"
        )


def complete_task(task_id: int) -> None:
    """
    Termine une tâche.
    """

    update_task(
        task_id,
        True
    )

    print("Tâche terminée ✅")


def remove_task(task_id: int) -> None:
    """
    Supprime une tâche.
    """

    delete_task(task_id)

    print("Tâche supprimée ✅")


def main() -> None:
    """
    Lance l'application TaskFlow en ligne de commande.
    """


    parser = argparse.ArgumentParser(
        description="Gestionnaire de tâches TaskFlow"
    )


    subparsers = parser.add_subparsers(
        dest="command"
    )


    add_parser = subparsers.add_parser("add")

    add_parser.add_argument(
        "task"
    )

    add_parser.add_argument(
        "--priority",
        type=int,
        default=1
    )

    add_parser.add_argument(
        "--due-date",
        default=None
    )


    subparsers.add_parser("list")


    done_parser = subparsers.add_parser("done")

    done_parser.add_argument(
        "number",
        type=int
    )


    remove_parser = subparsers.add_parser("remove")

    remove_parser.add_argument(
        "number",
        type=int
    )


    args = parser.parse_args()


    if args.command == "add":

        create_new_task(
            args.task,
            args.priority,
            args.due_date
        )


    elif args.command == "list":

        list_tasks()


    elif args.command == "done":

        complete_task(
            args.number
        )


    elif args.command == "remove":

        remove_task(
            args.number
        )


    else:

        parser.print_help()
import argparse
from datetime import datetime

from models import Task
from storage import (
    add_task,
    get_tasks,
    update_task,
    delete_task,
)


def validate_date(date: str | None) -> str | None:
    """
    Vérifie que la date respecte le format AAAA-MM-JJ.
    """

    if date is None:
        return None

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date

    except ValueError:
        raise ValueError("La date doit être au format AAAA-MM-JJ.")


def main() -> None:
    """
    Lance l'application TaskFlow en ligne de commande.
    """

    parser = argparse.ArgumentParser(description="Gestionnaire de tâches TaskFlow")

    subparsers = parser.add_subparsers(dest="command")

    # Commande add
    add_parser = subparsers.add_parser("add")

    add_parser.add_argument("task", help="Titre de la tâche")

    add_parser.add_argument(
        "--priority", type=int, default=1, help="Priorité entre 1 et 5"
    )

    add_parser.add_argument(
        "--due-date", default=None, help="Date au format AAAA-MM-JJ"
    )

    # Commande list
    subparsers.add_parser("list")

    # Commande done
    done_parser = subparsers.add_parser("done")

    done_parser.add_argument("number", type=int, help="Identifiant de la tâche")

    # Commande remove
    remove_parser = subparsers.add_parser("remove")

    remove_parser.add_argument("number", type=int, help="Identifiant de la tâche")

    args = parser.parse_args()

    try:
        if args.command == "add":
            if not args.task.strip():
                print("Erreur : le titre ne peut pas être vide.")
                return

            if args.priority < 1 or args.priority > 5:
                print("Erreur : la priorité doit être comprise entre 1 et 5.")
                return

            task = Task(
                id=None,
                title=args.task,
                priority=args.priority,
                due_date=validate_date(args.due_date),
                done=False,
            )

            add_task(task)

            print("Tâche ajoutée avec succès")

        elif args.command == "list":
            tasks = get_tasks()

            if not tasks:
                print("La liste des tâches est vide")
                return

            for task in tasks:
                due_date = task.due_date if task.due_date else "Aucune"

                print(
                    f"{task.id} - "
                    f"{'✅' if task.done else '❌'} "
                    f"{task.title} "
                    f"(priorité {task.priority}) "
                    f"(échéance : {due_date})"
                )

        elif args.command == "done":
            if update_task(args.number, True):
                print("Tâche terminée ✅")
            else:
                print("Erreur : aucune tâche trouvée avec cet identifiant.")

        elif args.command == "remove":
            if delete_task(args.number):
                print("Tâche supprimée ✅")
            else:
                print("Erreur : aucune tâche trouvée avec cet identifiant.")

        else:
            parser.print_help()

    except ValueError as error:
        print(f"Erreur : {error}")

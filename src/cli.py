import argparse

from todo import (
    create_new_task,
    list_tasks,
    complete_task,
    remove_task
)


def main() -> None:
    """
    Lance l'application TaskFlow en ligne de commande.
    """

    parser = argparse.ArgumentParser(
        description="Gestionnaire de tâches TaskFlow"
    )

    subparsers = parser.add_subparsers(dest="command")


    # Commande add
    add_parser = subparsers.add_parser("add")

    add_parser.add_argument(
        "task",
        help="Titre de la tâche"
    )

    add_parser.add_argument(
        "--priority",
        type=int,
        default=1,
        help="Priorité de la tâche entre 1 et 5"
    )

    add_parser.add_argument(
        "--due-date",
        default=None,
        help="Date d'échéance au format AAAA-MM-JJ"
    )


    # Commande list
    subparsers.add_parser("list")


    # Commande done
    done_parser = subparsers.add_parser("done")

    done_parser.add_argument(
        "number",
        type=int
    )


    # Commande remove
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

        complete_task(args.number)


    elif args.command == "remove":

        remove_task(args.number)


    else:

        parser.print_help()
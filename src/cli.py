import argparse

from todo import create_new_task, list_tasks, complete_task, remove_task


def main() -> None:
    """
    Lance l'application TaskFlow en ligne de commande.
    """

    parser = argparse.ArgumentParser(
        description="Gestionnaire de tâches TaskFlow"
    )

    subparsers = parser.add_subparsers(dest="command")


    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("task")


    subparsers.add_parser("list")


    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("number", type=int)


    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("number", type=int)


    args = parser.parse_args()


    if args.command == "add":

        create_new_task(
            args.task,
            priority=1
        )


    elif args.command == "list":

        list_tasks()


    elif args.command == "done":

        complete_task(args.number)


    elif args.command == "remove":

        remove_task(args.number)


    else:

        parser.print_help()
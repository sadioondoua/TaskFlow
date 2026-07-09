import csv

from storage import get_tasks


def export_tasks_csv(filename: str = "tasks.csv") -> None:
    """
    Exporte toutes les tâches dans un fichier CSV.
    """

    tasks = get_tasks()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "id",
                "title",
                "priority",
                "due_date",
                "done",
                "holiday",
            ]
        )

        for task in tasks:
            writer.writerow(
                [
                    task.id,
                    task.title,
                    task.priority,
                    task.due_date,
                    task.done,
                    task.holiday,
                ]
            )

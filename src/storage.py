import json


def save_tasks(tasks: list) -> None:
    """
    Sauvegarde les tâches dans le fichier JSON.
    """

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def load_tasks() -> list:
    """
    Charge les tâches depuis le fichier JSON.
    """

    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
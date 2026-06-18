from storage import save_tasks, load_tasks


my_tasks = load_tasks()


def add_task(task: str) -> None:
    """
    Ajoute une nouvelle tâche.
    """

    my_tasks.append(task)

    save_tasks(my_tasks)

    print("Tâche ajoutée avec succès")


def list_tasks() -> None:
    """
    Affiche toutes les tâches.
    """

    if len(my_tasks) == 0:
        print("La liste des tâches est vide")

    else:
        for numero, tache in enumerate(my_tasks):
            print(f"{numero} - {tache}")


def complete_task(number: int) -> None:
    """
    Marque une tâche comme terminée.
    """

    try:
        tache = my_tasks[number]

        my_tasks[number] = "✅ " + tache

        save_tasks(my_tasks)

        print("Tâche terminée ✅")

    except IndexError:
        print("Cette tâche n'existe pas")


def delete_task(number: int) -> None:
    """
    Supprime une tâche.
    """

    try:
        del my_tasks[number]

        save_tasks(my_tasks)

        print("Tâche supprimée ✅")

    except IndexError:
        print("Cette tâche n'existe pas")
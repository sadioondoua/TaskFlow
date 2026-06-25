from todo import add_task, list_tasks, complete_task, delete_task


def menu():
    """
    Affiche le menu principal de TaskFlow.
    """

    choice = ""

    while choice != "5":

        print("\n--------- TASKFLOW ----------")
        print("1 - Ajouter une tâche")
        print("2 - Voir les tâches")
        print("3 - Terminer une tâche")
        print("4 - Supprimer une tâche")
        print("5 - Quitter")

        choice = input("Choisir une option : ")

        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("A bientôt")

        else:
            print("Choix invalide")

            
if __name__ == "__main__":
    menu()

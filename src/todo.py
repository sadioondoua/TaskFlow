import json

my_tasks = []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(my_tasks, file)


def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)


my_tasks = load_tasks()


def add_task():

    task = input("Ajouter la tache:  ")

    print("tache ajoutee avec success")

    my_tasks.append(task)

    save_tasks()


def list_tasks():

    if len(my_tasks) == 0:
        print("\n< La liste des taches est actuellement vide >")

    else:

        for numero, tache in enumerate(my_tasks):
            print(f"{numero} - {tache}")

        input("Appuie sur entree pour revenir au menu : ")


def complete_task():


    for numero, tache in enumerate(my_tasks):
        print(f"{numero} - {tache}")

    num = int(input("Saisir le chiffre correspondant de la tache a terminer : "))

    tache_choisie = my_tasks[num]

    my_tasks[num] = "✅ " + tache_choisie

    save_tasks()

    print("Tache terminee ✅")


def delete_task():


    for numero, tache in enumerate(my_tasks):
        print(f"{numero} - {tache}")

    num = int(input("Saisir le chiffre de la tâche à supprimer : "))

    reponse=input("voulez-vous vriment supprimer ? (oui/non):  ")  

    if reponse== "oui":
       del my_tasks[num]
       save_tasks()
       print("Tâche supprimée ✅")

    else:
      print("Suppression annulee.")



def menu():

    choice = ""

    while choice != "5":

        print("\n   BIENVENUE DANS NOTRE GESTIONNAIRE DE TACHES")
        print("\n--------- TASKFLOW ----------")

        print("\n1* Ajouter une tâche")
        print("2* Lister les tâches")
        print("3* Terminer une tâche")
        print("4* Supprimer une tâche")
        print("5* Quitter")

        choice = input("Entrez une option (1/2/3/4/5): ")

        print("Tu as choisi: ", choice)

        if choice == "1":
            add_task()

        if choice == "2":
            list_tasks()

        if choice == "3":
            complete_task()

        if choice == "4":
            delete_task()
        
        if choice == "5":
            print("A binetot!!!")



       
    

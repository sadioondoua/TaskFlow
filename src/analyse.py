import pandas as pd


def analyse_tasks(csv_file: str = "tasks.csv") -> None:
    """
    Analyse les tâches exportées avec pandas.
    """

    df = pd.read_csv(csv_file)

    print("\n===== Nombre de tâches par statut =====")
    print(df["done"].value_counts())

    print("\n===== Nombre de tâches par priorité =====")
    print(df["priority"].value_counts())

    print("\n===== Nombre total de tâches =====")
    print(len(df))

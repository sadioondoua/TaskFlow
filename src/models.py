class Task:
    """
    Représente une tâche.
    """

    def __init__(self, title: str, done: bool = False):
        """
        Crée une tâche.

        Args:
            title: nom de la tâche
            done: état de la tâche
        """

        self.title = title
        self.done = done
class Task:
    """
    Représente une tâche.
    """

    def __init__(self, title: str, done: bool = False):
        self.title = title
        self.done = done
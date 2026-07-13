from dataclasses import dataclass
from typing import Optional
 

@dataclass
class Task:
    """
    Représente une tâche de TaskFlow.
    """

    id: Optional[int] = None
    title: str = ""
    priority: int = 1
    due_date: Optional[str] = None
    done: bool = False
    holiday: bool = False

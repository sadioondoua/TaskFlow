from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    priority: int
    due_date: Optional[str] = None
    done: bool = False
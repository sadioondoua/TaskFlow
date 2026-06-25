import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from todo import create_new_task, complete_task, remove_task
from storage import get_tasks, clear_tasks


def test_add_task():

    clear_tasks()

    create_new_task(
        "Faire les courses",
        1
    )

    tasks = get_tasks()

    assert tasks[0].title == "Faire les courses"



def test_complete_task():

    clear_tasks()

    create_new_task(
        "Apprendre Python",
        1
    )

    tasks = get_tasks()

    complete_task(tasks[0].id)

    tasks = get_tasks()

    assert tasks[0].done is True



def test_delete_task():

    clear_tasks()

    create_new_task(
        "Supprimer moi",
        1
    )

    tasks = get_tasks()

    remove_task(tasks[0].id)

    tasks = get_tasks()

    assert len(tasks) == 0
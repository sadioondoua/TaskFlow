import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "src")
)

from models import Task
from storage import (
    create_table,
    add_task,
    get_tasks,
    update_task,
    delete_task,
    clear_tasks,
)


def setup_function():
    create_table()
    clear_tasks()


def test_add_task():
    task = Task(
        title="Apprendre Python",
        priority=1,
    )

    add_task(task)

    tasks = get_tasks()

    assert len(tasks) == 1
    assert tasks[0].title == "Apprendre Python"


def test_list_tasks():
    add_task(
        Task(
            title="Test liste",
            priority=2,
        )
    )

    tasks = get_tasks()

    assert len(tasks) == 1
    assert tasks[0].title == "Test liste"


def test_done_task():
    add_task(
        Task(
            title="Projet",
            priority=1,
        )
    )

    task = get_tasks()[0]

    result = update_task(task.id, True)

    tasks = get_tasks()

    assert result is True
    assert tasks[0].done is True


def test_delete_task():
    add_task(
        Task(
            title="Supprimer",
            priority=1,
        )
    )

    task = get_tasks()[0]

    result = delete_task(task.id)

    assert result is True
    assert len(get_tasks()) == 0


def test_priority():
    add_task(
        Task(
            title="Urgent",
            priority=5,
        )
    )

    tasks = get_tasks()

    assert tasks[0].priority == 5


def test_due_date():
    add_task(
        Task(
            title="Date",
            priority=1,
            due_date="2026-07-01",
        )
    )

    tasks = get_tasks()

    assert tasks[0].due_date == "2026-07-01"


def test_default_done():
    add_task(
        Task(
            title="État",
            priority=1,
        )
    )

    tasks = get_tasks()

    assert tasks[0].done is False


def test_delete_unknown_task():
    result = delete_task(999)

    assert result is False

from src import todo


def test_add_task():
    todo.my_tasks.clear()

    todo.add_task("Faire les courses")

    assert "Faire les courses" in todo.my_tasks


def test_complete_task():
    todo.my_tasks.clear()

    todo.add_task("Apprendre Python")

    todo.complete_task(0)

    assert todo.my_tasks[0] == "✅ Apprendre Python"


def test_delete_task():
    todo.my_tasks.clear()

    todo.add_task("Supprimer moi")

    todo.delete_task(0)

    assert len(todo.my_tasks) == 0
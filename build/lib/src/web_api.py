from fastapi import FastAPI

from src.models import Task
from src.storage import add_task, get_tasks, update_task

app = FastAPI(
    title="TaskFlow API",
    description="API Web de TaskFlow",
    version="1.0",
)


@app.get("/")
def home():
    return {"message": "Bienvenue sur TaskFlow API !"}


@app.get("/tasks")
def list_tasks():
    return get_tasks()


@app.post("/tasks")
def create_task(task: Task):
    add_task(task)
    return {"message": "Tâche ajoutée avec succès."}


@app.patch("/tasks/{task_id}/done")
def done_task(task_id: int):
    success = update_task(task_id, True)

    if success:
        return {"message": "Tâche terminée."}

    return {"message": "Tâche introuvable."}

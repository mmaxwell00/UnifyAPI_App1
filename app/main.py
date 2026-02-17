from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Task Manager API", version="1.0.0")


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: Optional[str] = None


tasks_db = []
task_id_counter = 1


@app.get("/")
def read_root():
    return {
        "message": "Welcome to Task Manager API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    global task_id_counter

    task_dict = task.dict()
    task_dict["id"] = task_id_counter
    task_dict["created_at"] = datetime.utcnow().isoformat()

    tasks_db.append(task_dict)
    task_id_counter += 1

    return task_dict


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    for i, existing_task in enumerate(tasks_db):
        if existing_task["id"] == task_id:
            task_dict = task.dict(exclude={"id", "created_at"})
            task_dict["id"] = task_id
            task_dict["created_at"] = existing_task["created_at"]
            tasks_db[i] = task_dict
            return task_dict
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")

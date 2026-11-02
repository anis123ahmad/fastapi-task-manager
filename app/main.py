
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


# Temporary storage
tasks = []
next_task_id = 1


# Pydantic model for creating a task
class TaskCreate(BaseModel):
    title: str
    description: str | None = None


# Pydantic model for updating a task
class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    completed: bool


# Pydantic model for API responses
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Task Manager",
        "status": "Application is running"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "task-manager"
    }


# CREATE: Add a new task
@app.post(
    "/tasks/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):

    global next_task_id

    new_task = {
        "id": next_task_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks.append(new_task)
    next_task_id += 1

    return new_task


# READ: Get all tasks
@app.get("/tasks/", response_model=list[TaskResponse])
def get_tasks():
    return tasks


# READ: Get one task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# UPDATE: Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskUpdate):

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed

            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# DELETE: Delete an existing task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):
        if task["id"] == task_id:

            deleted_task = tasks.pop(index)

            return {
                "message": "Task deleted successfully",
                "task": deleted_task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

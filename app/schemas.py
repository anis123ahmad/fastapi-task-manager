from enum import Enum
from pydantic import BaseModel, ConfigDict


# Allowed priority values
class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# Schema for creating a task
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: Priority = Priority.MEDIUM


# Schema for updating a task
class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    completed: bool
    priority: Priority = Priority.MEDIUM


# Schema for returning a task
class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    completed: bool
    priority: Priority
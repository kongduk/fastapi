from pydantic import BaseModel

class Todo(BaseModel):
    task: str

class TodoResponse(Todo):
    todo_id: int
    content: str
    created_at: str

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI() # Create an instance of FastAPI

todos = [] # Create an empty list to store todos, in memory db

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/todos")
def get_todos():
    return todos

@app.get("todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return {"error": "Todo not found"}
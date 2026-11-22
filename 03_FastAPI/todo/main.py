from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from models import TodoModel
from database import Sessionlocal, engine
from sqlalchemy.orm import Session

app = FastAPI() # Create an instance of FastAPI

TodoModel.metadata.create_all(bind=engine) # Create the table in the databse

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", response_model=List[TodoModel])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

@app.get("todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict()) # Append the todo to the list
    return todos[-1] # Return the last todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}

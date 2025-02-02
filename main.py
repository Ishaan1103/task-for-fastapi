from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Temporary database
fake_db = []

# Data model
class Todo(BaseModel):
    task: str
    completed: bool = False

# Create
@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo):
    fake_db.append(todo)
    return todo

# Read All
@app.get("/todos/", response_model=List[Todo])
async def get_todos():
    return fake_db

# Read One
@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    try:
        return fake_db[todo_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")

# Update
@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, new_todo: Todo):
    try:
        fake_db[todo_id] = new_todo
        return new_todo
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")

# Delete
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    try:
        del fake_db[todo_id]
        return {"message": "Todo deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")
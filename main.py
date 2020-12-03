from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
    date: str


app = FastAPI()


"""Criação de rotas"""

all_todo = []


@app.get("/")
async def welcome():
    return {"What I need": "to do?"}


@app.post("/todo/")
async def create_todo(todo: Todo):
    all_todo.append(todo)
    return todo


@app.get("/todo/", response_model=List[Todo])
async def get_all():
    return all_todo


@app.get("/todo/{id}")
async def get_todo(id: int):

    try:
        return all_todo[id]

    except IndexError:
        raise HTTPException(status_code=404, detail="To do not found")


@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):

    try:
        all_todo[id] = todo
        return all_todo[id]

    except IndexError:
        raise HTTPException(status_code=404, detail="To do not found")


@app.delete('/todo/{id}')
async def delete_todo(id: int):

    try:
        item = all_todo[id]
        all_todo.pop(id)
        return item

    except IndexError:
        raise HTTPException(status_code=404, detail="To do not found")
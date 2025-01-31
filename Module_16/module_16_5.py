from fastapi import FastAPI, Path, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from pydantic import BaseModel
from typing import List


app = FastAPI()
templates = Jinja2Templates(directory="templates")

users_db = {"0": "Имя: {username}, возраст: {age}"}
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(request: Request, user_id) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[int(user_id)]})
    except IndexError:
        raise HTTPException(status_code=404, detail="user not found")


@app.get("/user/{username}/{age}")
async def id_paginator(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> dict:
    return {"message": f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(user_: User) -> User:
    user_.id = len(users)+1
    users.append(user_)
    return user_


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f'User {user_id} is deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

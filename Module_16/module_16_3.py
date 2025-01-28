from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users_db = {"0": "Имя: {username}, возраст: {age}"}


@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id: int = Path(ge=1, le=100, description='Enter User ID')) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def id_paginator(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> dict:
    return {"message": f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get("/user")
async def get_all_users() -> dict:
    return users_db


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    users_db[current_index] = f"Имя: {username}, Возраст: {age}"
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    users_db[user_id] = f"Имя: {username}, Возраст: {age}"
    return f'User {user_id} is updated'


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users_db.pop(user_id)
    return f'User {user_id} is deleted'

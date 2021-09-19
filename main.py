from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*","http://192.168.1.7:1234"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST","PUT","GET","DELETE"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "World"}
from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User, UserCount
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from fastapi import Form
from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)


@app.get(
    "/users",
    tags=["users"],
    response_model=List[User],
    description="Get a list of all users",
)
def get_users():
    return conn.execute(users.select()).fetchall()


@app.get("/users/count", tags=["users"], response_model=UserCount)
def get_users_count():
    result = conn.execute(select([func.count()]).select_from(users))
    return {"total": tuple(result)[0][0]}


@app.get(
    "/users/{id}",
    tags=["users"],
    response_model=User,
    description="Get a single user by Id",
)
async def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@app.post("/users", tags=["users"], response_model=User, description="Create a new user")
async def create_user(id:int=Form(...),username:str=Form(...),password:str=Form(...),email:str=Form(...),avtSrc:str=Form(...)):
    print(new_user)
    new_user = {"id":id,"name": username, "email": email,"avtSrc":avtSrc}
    print(new_user)
    new_user["password"] = f.encrypt(password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return new_user


@app.put(
    "/users/{id}", tags=["users"], response_model=User, description="Update a User by Id"
)
async def update_user(user: User, id: int):
    conn.execute(
        users.update()
        .values(name=user.name, email=user.email, password=user.password,avtSrc=user.avtSrc)
        .where(users.c.id == id)
    )
    return conn.execute(users.select().where(users.c.id == id)).first()


@app.delete("/{id}", tags=["users"], status_code=HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

# app.include_router(user)
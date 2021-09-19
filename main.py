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
app.include_router(user)
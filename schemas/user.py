from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str
    avtSrc:str

class UserCount(BaseModel):
    total: int

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    avtSrc:str

class UserUpdate(BaseModel):
    name: str
    email: str
    avtSrc:str
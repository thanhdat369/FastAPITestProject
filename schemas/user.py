from typing import Optional
from pydantic import BaseModel
class User(BaseModel):
    username:str
    description:Optional[str]
    avtSrc:Optional[str]

class UserCreate(User):
    password:str

class UserInDB(UserCreate):
    isDiasble:bool
    roleID:str

class UserAuth(BaseModel):
    username:str
    password:str
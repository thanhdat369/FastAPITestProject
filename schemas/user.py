from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
    username:str
    description:Optional[str]
    avtSrc:Optional[str]


class UserCreate(User):
    password:str

class UserInDB(UserCreate):
    isDiasble:bool
    roleID:str
from pydantic import BaseModel
from typing import Optional
class Product(BaseModel):
    id:str
    name:str
    imageScr:Optional[str]
    description:Optional[str]
    price:Optional[float]

class ProductInDB(Product):
    categoryID:str

class Category(BaseModel):
    id:str
    name:str
    description:str
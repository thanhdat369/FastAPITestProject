from datetime import datetime
from pydantic import BaseModel
class Bill(BaseModel):
   id:str
   username:str
   total:float
   description:str

class BillInDB(Bill):
   dateCreated:datetime


class BillDetail(BaseModel):
    productID:str
    description:str

class BillDetailInDB(BillDetail):
   dateCreated:datetime
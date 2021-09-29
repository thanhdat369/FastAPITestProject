from db.db_config import meta,engine
import datetime
from sqlalchemy import Column,String,Integer,ForeignKey,Float,Table,Boolean,DateTime,Float


roles = Table(
    'role', meta,
    Column('id',String(30),primary_key=True),
    Column('details',String(255))
)

users = Table(
    'user',meta,
    Column('username',String(255),primary_key=True,nullable=False),
    Column('password',String(255),nullable=False),
    Column('description',String(255)),
    Column('avtSrc',String(255),nullable=True),
    Column('roleID',String(30),ForeignKey('role.id')),
    Column('isDisable',Boolean),
)

category = Table(
    'category',meta,
    Column('id',String(30),primary_key=True),
    Column('name',String(255)),
    Column('description',String(255))
)
product = Table(
    'product',meta,
    Column('id',String(255),primary_key=True),
    Column('name',String(255),nullable=False),
    Column('imageScr',String(255)),
    Column('description',String(255),nullable=True),
    Column('categoryID',String(30),ForeignKey('category.id')),
    Column('price',Float),
)

bill = Table(
    'bill',meta,
    Column('id',String(255),primary_key=True),
    Column('username',String(30),ForeignKey('user.username')),
    Column('total',Float),
    Column('description',String(255),nullable=True),
    Column('dateCreated',DateTime, onupdate=datetime.datetime.now)
)

bill_detail = Table(
    'bill_detail',meta,
    Column('productID',String(255),ForeignKey('product.id'),primary_key=True),
    Column('billID',String(255),ForeignKey('bill.id'),primary_key=True),
    Column('pricePerUnit',Float,nullable=False),
    Column('quantity',Integer,nullable=False)
    
)


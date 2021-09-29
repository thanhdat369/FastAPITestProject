from fastapi import Depends,status,HTTPException
from fastapi.routing import APIRouter

from typing import List

from api.dependencies.user import get_current_active_user,get_current_active_admin
from schemas.user import User,UserInDB,UserCreate
import services.user as user_services
router = APIRouter()

@router.get("/",response_model=List[User])
async def get_all_user(current_user: UserInDB = Depends(get_current_active_admin)):
    return user_services.get_users()

@router.get("/{username}",response_model=User)
async def get_all_user(username:str,current_user: UserInDB = Depends(get_current_active_user)):
    if current_user.roleID=="ADMIN" or current_user.username == username:
        return user_services.get_user_by_username(username)
    else:
        raise HTTPException(status_code=401, detail="No Permission")
    
@router.post("/",response_model=User)
async def create_user(user_create:UserCreate):
    return user_services.create_user(user_create)

@router.delete("/{username}")
async def delete_user(username:str,current_user: UserInDB = Depends(get_current_active_user)):
    if current_user.roleID=="ADMIN" or current_user.username == username:
        return user_services.del_user(username)
    else:
        raise HTTPException(status_code=401, detail="No Permission")


@router.put("/{username}")
async def update_user(username:str,user_update:User,current_user: UserInDB = Depends(get_current_active_user)):
    if current_user.roleID=="ADMIN" or current_user.username == username:
        return user_services.update_user(username,user_update)
    else:
        raise HTTPException(status_code=401, detail="No Permission")

@router.put("/{username}/activate")
async def activate_user(username:str,current_user: UserInDB = Depends(get_current_active_admin)):
    return user_services.actviate_user(username)    
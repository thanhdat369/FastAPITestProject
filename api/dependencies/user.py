
from fastapi import Depends,HTTPException
from schemas.jwt import Token,TokenData
from schemas.user import UserInDB
from services.jwt import get_current_user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.isDisable:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def get_current_active_admin(current_user: UserInDB = Depends(get_current_active_user)):
    if current_user.roleID != "ADMIN":
        raise HTTPException(status_code=401, detail="No Permission")
    return current_user


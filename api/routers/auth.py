from fastapi import Depends,status,HTTPException
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from schemas.jwt import Token,TokenData
from datetime import timedelta
from services.jwt import create_access_token
from services.user import aut_user

from schemas.user import User,UserInDB,UserAuth

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(form:OAuth2PasswordRequestForm=Depends()):
    user = aut_user(form.username,form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=20)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

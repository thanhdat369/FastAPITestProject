from fastapi import FastAPI
from api.routers.api import api_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
ALLOWED_HOSTS =["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pages.auth import user

app = FastAPI()

origin = [
    "http://localhost:3000",
]

app.add_middleware(
CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
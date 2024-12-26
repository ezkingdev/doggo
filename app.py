# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import create_db_and_tables
from routes.router import router

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# API routes setup will go here

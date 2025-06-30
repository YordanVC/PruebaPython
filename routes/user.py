from fastapi import APIRouter
from config.db import conn
from models.user import users

user = APIRouter()


@user.get("/users")
def read_root():
    return conn.execute(users.select()).fetchall()


@user.get("/users")
def read_root():
    return {"message": "Hola desde user FastAPI"}


@user.get("/users")
def read_root():
    return {"message": "Hola desde user FastAPI"}


@user.get("/users")
def read_root():
    return {"message": "Hola desde user FastAPI"}


@user.get("/users")
def read_root():
    return {"message": "Hola desde user FastAPI"}

from fastapi import APIRouter, HTTPException
from config.db import conn, engine
from models.user import users
from schemas.user import User

# Para cifrar la contraseña
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get("/users", response_model=list[User])
def read_root():
    return conn.execute(users.select()).fetchall()


@user.post("/users", response_model=User)
def create_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": f.encrypt(user.password.encode("utf-8")).decode("utf-8")
    }
    print(new_user)
    with engine.begin() as conn:
        response = conn.execute(users.insert().values(new_user))
        inserted_user = conn.execute(
            users.select().where(
                users.c.id == response.lastrowid)
        ).first()

    return inserted_user._asdict()


@user.get("/users/{id}", response_model=User)
def get_user_by_id(id: int):
    inserted_user = conn.execute(
        users.select().where(
            users.c.id == id)
    ).first()
    if inserted_user:
        return dict(inserted_user._mapping)
    else:
        raise HTTPException(status_code=404, detail="User not found")


@user.delete("/users/{id}")
def delete_user(id: int):
    result = conn.execute(
        users.delete().where(
            users.c.id == id)
    )
    return ("user deleted" if result.rowcount > 0
            else {"error": "User not found"})


@user.put("/users/{id}")
def update_user(id: int, user: User):
    result = conn.execute(
        users.update().values(
            name=user.name,
            email=user.email,
            password=f.encrypt(user.password.encode("utf-8")).decode("utf-8")
        ).where(
            users.c.id == id)
    )
    return (get_user_by_id(id) if result.rowcount > 0
            else {"error": "User not found"})

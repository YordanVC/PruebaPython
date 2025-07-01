from fastapi import FastAPI
from controller.user import user

app = FastAPI(
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations with users"
        }
    ]
)
app.include_router(user)

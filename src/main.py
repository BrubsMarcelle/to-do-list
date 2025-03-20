from fastapi import FastAPI
from src.shared.database import engine, Base
from src.todolist.router.router import router as todolist_router

app = FastAPI()

app.include_router(todolist_router)

Base.metadata.create_all(bind=engine)
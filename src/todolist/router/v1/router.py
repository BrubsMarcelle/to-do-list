from fastapi import APIRouter
from .todolist_router import router as todo_router

router = APIRouter(prefix='/v1')
router.include_router(todo_router)
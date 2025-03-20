from fastapi import APIRouter
from .v1.router import router as v1_router

router = APIRouter(prefix='/api/to-do-list')

router.include_router(v1_router)
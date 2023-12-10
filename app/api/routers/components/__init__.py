from fastapi import APIRouter

from .bridges import router as bridges_router

router = APIRouter(prefix='/components')
router.include_router(bridges_router)

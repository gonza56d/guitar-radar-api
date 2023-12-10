from fastapi import APIRouter

from app.core.models.guitars import Bridge

router = APIRouter(prefix='/bridges', tags=['bridges'])


@router.post('')
async def post_bridge(
        bridge: Bridge
):
    return {'message': 'Hello world'}

from fastapi import APIRouter


router = APIRouter(prefix='/hello_world', tags=['hello_world'])


@router.get('')
async def get_hello_world():
    return {'message': 'Hello world'}

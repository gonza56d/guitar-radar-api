from fastapi import FastAPI


api = FastAPI()


@api.get('/')
async def hello_world():
    return {'message': 'Hello world'}

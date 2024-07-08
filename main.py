import uuid
from fastapi import FastAPI, Request
from app.routes import BasicRouters
from core import MongoConnection

app = FastAPI()
MongoConnection.Create()


@app.middleware("http")
async def unauthMiddleware(request: Request, callNext):
    requestId = str(uuid.uuid4())
    headers = {"requestId": requestId}
    request.state.headers = headers
    response = callNext(request)
    return response


app.include_router(BasicRouters)


@app.get("/")
def main():
    return "Hello from Image Compressor App"

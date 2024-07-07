from fastapi import FastAPI
from app.routes import BasicRouters

app = FastAPI()

app.include_router(BasicRouters)


@app.get("/")
def main():
    return "Hello from Image Compressor App"

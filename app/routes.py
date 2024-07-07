from fastapi import APIRouter
from app.endpoints import images_crud

BasicRouters = APIRouter(prefix="/image_compressor/v1")
BasicRouters.include_router(images_crud.Router)

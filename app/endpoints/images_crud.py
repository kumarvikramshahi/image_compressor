from fastapi import APIRouter
from schema.schema import (
    UploadImagesRequest,
    ImageProcessingStatusRequest,
    GenericResponse,
)

Router = APIRouter()


@Router.post("/upload_images", response_model=GenericResponse)
async def UploadImages(reqItem: UploadImagesRequest):
    csvFile = await reqItem.CsvFile.read()
    return GenericResponse(data={"message": "file uploaded successfully"})


@Router.post("/image_processing_status", response_model=GenericResponse)
async def ImageProcessingStatus(reqItem: ImageProcessingStatusRequest):
    return GenericResponse(data="image_processing_status")

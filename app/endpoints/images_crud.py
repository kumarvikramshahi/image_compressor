import csv
import uuid
from fastapi import APIRouter, UploadFile, File
from typing import Annotated
from io import StringIO
from schema.schema import (
    ImageProcessingStatusRequest,
    GenericResponse,
)


Router = APIRouter()


@Router.post("/upload_images", response_model=GenericResponse)
async def UploadImages(csv_file: Annotated[UploadFile, File()]):
    csvFile = await csv_file.read()
    csvStringData = str(csvFile, "utf-8")
    csvData = csv.reader(StringIO(csvStringData))
    print(list(csvData))
    return GenericResponse(data={"message": "file uploaded successfully"})


@Router.post("/image_processing_status", response_model=GenericResponse)
async def ImageProcessingStatus(reqItem: ImageProcessingStatusRequest):
    return GenericResponse(data="image_processing_status")

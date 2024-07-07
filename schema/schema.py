from pydantic import BaseModel, Field
from typing import Any, Annotated
from fastapi import UploadFile, File


class UploadImagesRequest(BaseModel):
    CsvFile: Annotated[UploadFile, File()] = Field(alias="csv_file")


class UploadImagesCsvFileDataFormat(BaseModel):
    pass


class ImageProcessingStatusRequest(BaseModel):
    RequestId: str = Field(alias="request_id")


class GenericResponse(BaseModel):
    Data: Any = Field(alias="data")

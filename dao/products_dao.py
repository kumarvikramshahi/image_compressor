from pydantic import BaseModel, Field
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorCollection
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from core import MongoConnection
from utils.time_utils import TimeUtils
from schema.enum_list import ImageProcessingStatus


class ProductImageModel(BaseModel):
    Name: str = Field(alias="name")
    RequestId: str = Field(alias="request_id")
    InputImages: list[str] = Field(alias="input_images")
    OutputImages: Optional[list[str]] = Field(alias="output_images", default=None)
    Status: ImageProcessingStatus = Field(alias="status")
    CreatedAt: int = Field(alias="created_at")
    UpdatedAt: int = Field(alias="updated_at")


class ProductImageDTO(ProductImageModel):
    Id: str = Field(alias="_id")


class UpdateProductImageDTO(ProductImageModel):
    Name: Optional[str] = Field(alias="name", default=None)
    RequestId: Optional[str] = Field(alias="request_id", default=None)
    InputImages: Optional[list[str]] = Field(alias="input_images", default=None)
    OutputImages: Optional[list[str]] = Field(alias="output_images", default=None)
    Status: Optional[str] = Field(alias="status", default=None)


class ProductDB:
    _collectionName: str = "product_image"
    MongoProductImageColl: AsyncIOMotorCollection = None

    def __init__(self) -> None:
        self.MongoProductImageColl = MongoConnection.ProductDB[self._collectionName]

    async def CreateDocument(self, insertData: ProductImageDTO) -> str:
        insertData.CreatedAt = TimeUtils().currentUtcEpochTimestamp()
        insertData.UpdatedAt = TimeUtils().currentUtcEpochTimestamp()

        encodedInsertData = jsonable_encoder(
            obj=ProductImageModel(
                name=insertData.Name,
                request_id=insertData.RequestId,
                input_images=insertData.InputImages,
                status=insertData.Status,
                created_at=insertData.CreatedAt,
                updated_at=insertData.UpdatedAt,
            ),
            exclude_none=True,
        )
        result = await self.MongoProductImageColl.insert_one(encodedInsertData)
        return str(result.inserted_id)

    async def UpdateDocument(self, id: str, updateData: UpdateProductImageDTO) -> None:
        updateData.UpdatedAt = TimeUtils().currentUtcEpochTimestamp()
        encodedUpdateData = jsonable_encoder(obj=updateData, exclude_none=True)
        await self.MongoFaceVectorColl.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": encodedUpdateData},
            return_document=True,
        )

    async def GetByRequestId(self, requestId: str) -> Optional[ProductImageDTO]:
        searchFilter = {"request_id": requestId}
        searchResult = await self.MongoProductImageColl.find_one(searchFilter)
        if searchResult is None:
            return None

        searchResult["_id"] = str(searchResult["_id"])
        response = ProductImageDTO(**searchResult)
        return response

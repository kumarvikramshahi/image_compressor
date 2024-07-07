from pydantic import BaseModel, Field
from typing import Optional


class ProductModel(BaseModel):
    Name: str = Field(alias="name")
    RequestId: str = Field(alias="request_id")
    InputImages: list[str] = Field(alias="input_images")
    OutputImages: Optional[list[str]] = Field(alias="output_images", default=None)
    Status: str = Field(alias="status")
    CreatedAt: int = Field(alias="created_at")
    UpdatedAt: int = Field(alias="updated_at")


class ProductDTO(ProductModel):
    Id: str = Field(alias="_id")


class UpdateProductDTO(ProductModel):
    Name: Optional[str] = Field(alias="name", default=None)
    RequestId: Optional[str] = Field(alias="request_id", default=None)
    InputImages: Optional[list[str]] = Field(alias="input_images", default=None)
    OutputImages: Optional[list[str]] = Field(alias="output_images", default=None)
    Status: Optional[str] = Field(alias="status", default=None)


class ProductCollection:
    def __init__(self) -> None:
        pass

    async def CreateDocument(self, insertData: ProductDTO):
        pass

    async def UpdateDocument(self, updateData: UpdateProductDTO):
        pass

    async def GetByRequestId(self, requestId: str):
        pass

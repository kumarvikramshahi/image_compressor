import logging
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config.settings import ConfigSettings


class MongoDbConnection:
    ProductDB: AsyncIOMotorDatabase
    Client: AsyncIOMotorClient

    def __init__(self) -> None:
        pass

    def Create(self) -> None:
        mongoUri = f"mongodb+srv://{ConfigSettings.MONGODB_USER}:{ConfigSettings.MONGODB_PASSWORD}@{ConfigSettings.MONGODB_HOST}/"
        if ConfigSettings.ENV_NAME == "dev":
            mongoUri = f"mongodb://{ConfigSettings.MONGODB_HOST}"
        self.Client = AsyncIOMotorClient(mongoUri)
        self.ProductDB = self.client[ConfigSettings.MONGODB_NAME]
        logging.info("Connected to the MongoDB database!")

    def Close(self) -> None:
        self.client.close()
        logging.info("Closed Mongo Connection")

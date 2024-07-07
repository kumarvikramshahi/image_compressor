import logging
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config.settings import ConfigSettings


class MongoDbConnection:
    VectorDb: AsyncIOMotorDatabase
    Client: AsyncIOMotorClient

    def __init__(self) -> None:
        pass

    def Create(self) -> None:
        mongoUri = f"mongodb+srv://{ConfigSettings.MONGODB_USER}:{ConfigSettings.MONGODB_PASSWORD}@{ConfigSettings.MONGODB_HOST}/"
        self.client = AsyncIOMotorClient(mongoUri)
        self.vectorDb = self.client[ConfigSettings.MONGODB_NAME]
        logging.info("Connected to the MongoDB database!")

    def Close(self) -> None:
        self.client.close()
        logging.info("Closed Mongo Connection")

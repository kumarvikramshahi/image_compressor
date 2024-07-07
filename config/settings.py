import os


class Settings:
    DEBUG = True
    SERVICE_NAME = "image_compressor"

    ENV_NAME = os.getenv("ENV_NAME")
    PORT = os.getenv("PORT")
    API_TIMEOUT = os.getenv("API_TIMEOUT")

    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_NAME = os.getenv("MONGODB_NAME")

    LOG_LEVEL = os.getenv("LOG_LEVEL")


ConfigSettings = Settings()

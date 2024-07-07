import requests

async def DownloadFile(imageUrl:str):
    response = requests.get(imageUrl)
    
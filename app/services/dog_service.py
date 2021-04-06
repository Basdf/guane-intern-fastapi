import httpx
from datetime import datetime


async def create_dog_data():
    return {
        "create_date": datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f"),
        "picture": await get_dogpicture(),
    }


async def get_dogpicture():
    url = "https://dog.ceo/api/breeds/image/random"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    return data["message"]

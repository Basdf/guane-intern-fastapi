import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable.
DOGS_COLLECTION = "dogs_collection"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.guane

dog_collection = database.get_collection(DOGS_COLLECTION)
dog_collection.create_index("name", unique=True)

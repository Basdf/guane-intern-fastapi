import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")
USERS_COLLECTION = "users_collection"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.guane

user_collection = database.get_collection(USERS_COLLECTION)
user_collection.create_index("id", unique=True)

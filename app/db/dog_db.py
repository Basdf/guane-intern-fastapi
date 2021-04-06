import motor.motor_asyncio
from decouple import config
from pymongo.errors import DuplicateKeyError

MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable.

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.guane

dog_collection = database.get_collection("dogs_collection")
dog_collection.create_index("name", unique=True)

# helpers


def dog_helper(dog) -> dict:
    return {
        "id": str(dog["_id"]),
        "id_user": dog["id_user"],
        "name": dog["name"],
        "picture": dog["picture"],
        "create_date": dog["create_date"],
        "is_adopted": dog["is_adopted"],
    }


# crud operations

# Retrieve all dogs present in the database
async def retrieve_dogs():
    dogs = []
    async for dog in dog_collection.find():
        dogs.append(dog_helper(dog))
    return dogs


# Retrieve a dog with a matching name
async def retrieve_dog_by_name(name: str) -> dict:
    dog = await dog_collection.find_one({"name": name})
    if dog:
        return dog_helper(dog)


# Retrieve a dog with a is_adopted is True
async def retrieve_dog_by_is_adopted() -> dict:
    dogs = []
    async for dog in dog_collection.find({"is_adopted": True}):
        dogs.append(dog_helper(dog))
    return dogs


# Add a new dog into to the database
async def add_dog(dog_data: dict) -> dict:
    dog = None
    try:
        dog = await dog_collection.insert_one(dog_data)
    except DuplicateKeyError:
        return dog
    new_dog = await dog_collection.find_one({"_id": dog.inserted_id})
    return dog_helper(new_dog)


# Update a dog with a matching ID
async def update_dog(name: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    dog = await dog_collection.find_one({"name": name})

    if dog:
        try:
            updated_dog = await dog_collection.update_one(
                {"name": name}, {"$set": data}
            )
        except DuplicateKeyError:
            return False
        if updated_dog:
            return True
        return False


# Delete a dog from the database
async def delete_dog(name: str):
    dog = await dog_collection.find_one({"name": name})
    if dog:
        await dog_collection.delete_one({"name": name})
        return True

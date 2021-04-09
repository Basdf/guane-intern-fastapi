from pymongo.errors import DuplicateKeyError

from app.db.dog_db import dog_collection

# helpers


def dog_helper(dog):
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
async def get_dogs_repository():
    dogs = []
    async for dog in dog_collection.find():
        dogs.append(dog_helper(dog))
    return dogs


# Retrieve a dog with a matching name
async def get_dog_by_name_repository(name: str):
    dog = await dog_collection.find_one({"name": name})
    if dog:
        return dog_helper(dog)


# Retrieve adopted dogs
async def get_adopted_dogs_repository():
    dogs = []
    async for dog in dog_collection.find({"is_adopted": True}):
        dogs.append(dog_helper(dog))
    return dogs


# Add a new dog into to the database
async def save_dog_repository(dog_data: dict):
    try:
        dog = await dog_collection.insert_one(dog_data)
    except DuplicateKeyError:
        return None
    new_dog = await dog_collection.find_one({"_id": dog.inserted_id})
    return dog_helper(new_dog)


# Update a dog with a matching name
async def update_dog_repository(name: str, data: dict):
    # Return None if an empty request body is sent.
    if len(data) < 1:
        return None

    dog = await dog_collection.find_one({"name": name})

    if dog:
        try:
            updated_dog = await dog_collection.update_one(
                {"name": name},
                {"$set": data},
            )
        except DuplicateKeyError:
            return None
        if updated_dog:
            dog = await dog_collection.find_one({"_id": dog["_id"]})
            return dog_helper(dog)
        return None


# Delete a dog from the database
async def delete_dog_repository(name: str):
    dog = await dog_collection.find_one({"name": name})
    if dog:
        await dog_collection.delete_one({"name": name})
        return dog_helper(dog)

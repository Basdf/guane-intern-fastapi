from pymongo.errors import DuplicateKeyError

from app.db.user_db import user_collection

# helpers


def user_helper(user):
    return {
        "id": str(user["id"]),
        "name": user["name"],
        "last_id": user["last_name"],
        "email": user["email"],
    }


# crud operations

# get all users present in the database
async def get_users_repository():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


# get a user with a matching ID
async def get_user_by_id_repository(id: str):
    user = await user_collection.find_one({"id": id})
    if user:
        return user_helper(user)


# save a new user into to the database
async def save_user_repository(user_data: dict):
    try:
        user = await user_collection.insert_one(user_data)
    except DuplicateKeyError:
        return None
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Update a user with a matching ID
async def update_user_repository(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    user = await user_collection.find_one({"id": id})

    if user:
        try:
            updated_user = await user_collection.update_one(
                {"id": id},
                {"$set": data},
            )
        except DuplicateKeyError:
            return None
        if updated_user:
            user = await user_collection.find_one({"id": id})
            return user_helper(user)
        return None


# Delete a user from the database
async def delete_user_repository(id: str):
    user = await user_collection.find_one({"id": id})
    if user:
        await user_collection.delete_one({"id": id})
        return user_helper(user)

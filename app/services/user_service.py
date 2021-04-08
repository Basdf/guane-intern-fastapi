from app.repository.user_repository import (
    get_users_repository,
    get_user_by_id_repository,
    save_user_repository,
    update_user_repository,
    delete_user_repository,
)
from app.models.user_model import (
    UserModel,
    UpdateUserModel,
    UserResponse,
    UserErrorResponse,
)


async def get_users_service():
    users = await get_users_repository()
    if users:
        return UserResponse(
            data=users,
            message="Users data retrieved successfully.",
        )
    return UserResponse(
        data=users,
        message="Empty list returned.",
    )


async def get_user_by_id_service(id: str):
    user = await get_user_by_id_repository(id)
    if user:
        return UserResponse(
            data=[user],
            message="User data retrieved successfully.",
        )
    return UserErrorResponse(
        error="An error occurred.",
        message="User doesn't exist.",
    )


async def post_user_service(user_data: UserModel):
    new_user = await save_user_repository(user_data.dict())

    if new_user:
        return UserResponse(
            data=[new_user],
            message="User added successfully.",
        )
    return UserErrorResponse(
        error="An error occurred",
        message="Repeated ID.",
    )


async def put_user_service(id: str, req: UpdateUserModel):
    req = {k: v for k, v in req.dict().items() if v is not None}

    user = await update_user_repository(id, req)
    if user:
        return UserResponse(
            data=[user],
            message="User updated successfully.",
        )
    return UserErrorResponse(
        error="An error occurred.",
        message="There was an error updating the user data.",
    )


async def delete_user_service(id: str):
    deleted_user = await delete_user_repository(id)
    if deleted_user:
        return UserResponse(
            data=[deleted_user],
            message="User deleted successfully",
        )
    return UserErrorResponse(
        error="An error occurred",
        message="User doesn't exist",
    )

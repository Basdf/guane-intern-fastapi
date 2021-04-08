from fastapi import FastAPI
from app.routes.dog_routes import router as DogRouter
from app.routes.user_routes import router as UserRouter
from app.routes.token_routes import router as TokenRouter

tags_metadata = [
    {
        "name": "Dog",
        "description": "Routes to manage all CRUD operations over Dog",
    },
    {
        "name": "User",
        "description": "Routes to manage all CRUD operations over User",
    },
    {
        "name": "Token",
        "description": "Routes to manage create JWT",
    },
]

app = FastAPI(
    title="guane-intern-fastapi",
    description="Technical test of guane Enterprises",
    version="1.0.0",
    docs_url="/api/documentation",
    openapi_url="/api/openapi.json",
    redoc_url=None,
    openapi_tags=tags_metadata,
)

app.include_router(DogRouter, tags=["Dog"], prefix="/api/dogs")
app.include_router(UserRouter, tags=["User"], prefix="/api/users")
app.include_router(TokenRouter, tags=["Token"], prefix="/api/Token")

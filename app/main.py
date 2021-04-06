from fastapi import FastAPI
from app.routes.dog_routes import router as DogRouter


app = FastAPI(
    title="guane-intern-fastapi",
    description="Prueba tecnica de guane Enterprises",
    version="1.0.0",
    docs_url="/api/docs",
)
app.include_router(DogRouter, tags=["Dog"], prefix="/api/dogs")

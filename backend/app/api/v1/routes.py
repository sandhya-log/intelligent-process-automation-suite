from fastapi import APIRouter
from backend.app.api.v1.endpoints import ingestion
from backend.app.api.v1.endpoints import processing



api_router = APIRouter()

api_router.include_router(ingestion.router)
api_router.include_router(processing.router)

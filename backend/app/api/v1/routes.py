from fastapi import APIRouter
from app.api.v1.endpoints import ingestion
from app.api.v1.endpoints import processing
from app.api.v1.endpoints import workflow
from app.services.persistence_service import save_document
from app.api.v1.endpoints import analytics
from app.api.v1.endpoints import chatbot

api_router = APIRouter()

api_router.include_router(ingestion.router)
api_router.include_router(processing.router)
api_router.include_router(workflow.router)
api_router.include_router(analytics.router)
api_router.include_router(chatbot.router)

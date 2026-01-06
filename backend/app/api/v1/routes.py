from fastapi import APIRouter
from backend.app.api.v1.endpoints import ingestion
from backend.app.api.v1.endpoints import processing
from backend.app.api.v1.endpoints import workflow
from backend.app.services.persistence_service import save_document
from backend.app.api.v1.endpoints import analytics
from backend.app.api.v1.endpoints import chatbot

api_router = APIRouter()

api_router.include_router(ingestion.router)
api_router.include_router(processing.router)
api_router.include_router(workflow.router)
api_router.include_router(analytics.router)
api_router.include_router(chatbot.router)

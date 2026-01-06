from fastapi import APIRouter, UploadFile, File
from backend.app.services.ingestion_service import ingest_document

router = APIRouter(prefix="/ingestion", tags=["Ingestion"])


@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    return ingest_document(file)

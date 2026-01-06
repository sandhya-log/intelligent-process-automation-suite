from fastapi import APIRouter
from backend.app.services.document_processing_service import process_document

router = APIRouter(prefix="/process", tags=["Processing"])


@router.post("/{document_id}")
def process_uploaded_document(document_id: str):
    # TEMP: file path mapping (will be improved later)
    file_path = f"uploaded_files/{document_id}"

    return process_document(document_id, file_path)

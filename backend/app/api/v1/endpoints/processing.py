from fastapi import APIRouter
from backend.app.services.document_processing_service import process_document
import os
from backend.app.core.logger import logger


router = APIRouter(prefix="/process", tags=["Processing"])


@router.post("/{document_id}")
def process_uploaded_document(document_id: str):
    # Find file by document_id
    upload_dir = "uploaded_files"
    matching_files = [
        f for f in os.listdir(upload_dir) if f.startswith(document_id)
    ]

    if not matching_files:
        return {"error": "File not found"}

    file_path = os.path.join(upload_dir, matching_files[0])

    return process_document(document_id, file_path)


@router.post("/{document_id}")
def process_uploaded_document(document_id: str):
    try:
        ...
        return process_document(document_id, file_path)
    except Exception as e:
        logger.error(f"Processing failed for {document_id}: {str(e)}")
        return {
            "status": "failed",
            "error": "Document processing failed"
        }
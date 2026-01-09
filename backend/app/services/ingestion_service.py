from fastapi import UploadFile
from app.utils.file_storage import save_file
from app.core.logger import logger


def ingest_document(file: UploadFile) -> dict:
    document_id = save_file(file)
    logger.info(f"Document uploaded: {document_id}")

    return {
        "document_id": document_id,
        "filename": file.filename,
        "status": "uploaded"
    }

    

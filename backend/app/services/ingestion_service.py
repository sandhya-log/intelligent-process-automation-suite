from fastapi import UploadFile
from backend.app.utils.file_storage import save_file


def ingest_document(file: UploadFile) -> dict:
    document_id = save_file(file)

    return {
        "document_id": document_id,
        "filename": file.filename,
        "status": "uploaded"
    }

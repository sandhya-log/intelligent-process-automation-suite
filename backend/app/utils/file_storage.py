import os
import uuid
from fastapi import UploadFile

BASE_UPLOAD_DIR = "uploaded_files"


def save_file(file: UploadFile) -> str:
    os.makedirs(BASE_UPLOAD_DIR, exist_ok=True)
    document_id = str(uuid.uuid4())

    file_path = os.path.join(BASE_UPLOAD_DIR, f"{document_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return document_id

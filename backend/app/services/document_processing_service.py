from backend.app.utils.ocr_engine import extract_text_from_file
from backend.app.services.persistence_service import save_document


# def process_document(document_id: str, file_path: str) -> dict:
#     extracted_text = extract_text_from_file(file_path)

#     return {
#         "document_id": document_id,
#         "extracted_text": extracted_text,
#         "status": "processed"
#     }


def process_document(document_id: str, file_path: str) -> dict:
    extracted_text = extract_text_from_file(file_path)

    save_document(
        document_id=document_id,
        filename=file_path,
        extracted_text=extracted_text,
        status="processed"
    )

    return {
        "document_id": document_id,
        "extracted_text": extracted_text,
        "status": "processed"
    }

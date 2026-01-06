from backend.app.utils.ocr_engine import extract_text_from_file


def process_document(document_id: str, file_path: str) -> dict:
    extracted_text = extract_text_from_file(file_path)

    return {
        "document_id": document_id,
        "extracted_text": extracted_text,
        "status": "processed"
    }

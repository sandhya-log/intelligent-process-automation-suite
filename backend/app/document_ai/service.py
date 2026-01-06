from .utils import extract_text, clean_text
from .repository import save_document_result
from .schemas import DocumentRequest, DocumentResponse


def process_document(data: DocumentRequest) -> DocumentResponse:
    # 1. Validate input
    if not data.file_path:
        raise ValueError("File path is required")

    # 2. Extract text
    raw_text = extract_text(data.file_path)

    # 3. Clean text
    processed_text = clean_text(raw_text)

    # 4. Save result
    document_id = save_document_result(
        file_path=data.file_path,
        extracted_text=processed_text
    )

    # 5. Return response
    return DocumentResponse(
        document_id=document_id,
        status="processed",
        text=processed_text
    )

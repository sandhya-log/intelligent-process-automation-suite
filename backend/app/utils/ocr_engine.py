from fastapi import UploadFile


def extract_text_from_file(file_path: str) -> str:
    """
    Temporary simple extractor.
    For now, we just return placeholder text.
    Real OCR (Tesseract) will be plugged in later.
    """
    return "Sample extracted text from document"

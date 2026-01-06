def evaluate_workflow(document_id: str, extracted_text: str) -> dict:
    """
    Simple rule-based workflow engine.
    """

    # Rule 1: OCR failed or empty
    if not extracted_text or extracted_text.strip() == "":
        return {
            "document_id": document_id,
            "decision": "REJECTED",
            "reason": "No readable text found"
        }

    # Rule 2: Invoice detection
    if "invoice" in extracted_text.lower():
        return {
            "document_id": document_id,
            "decision": "FLAGGED",
            "reason": "Invoice requires manual review"
        }

    # Default rule
    return {
        "document_id": document_id,
        "decision": "APPROVED",
        "reason": "No issues detected"
    }

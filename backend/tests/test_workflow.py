
from app.services.workflow_engine import evaluate_workflow



def test_empty_text_rejected():
    result = evaluate_workflow("doc-1", "")
    assert result["decision"] == "REJECTED"


def test_invoice_flagged():
    result = evaluate_workflow("doc-2", "invoice total amount")
    assert result["decision"] == "FLAGGED"


def test_normal_text_approved():
    result = evaluate_workflow("doc-3", "hello world")
    assert result["decision"] == "APPROVED"

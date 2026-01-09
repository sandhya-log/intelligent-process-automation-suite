from fastapi import APIRouter
from app.services.workflow_engine import evaluate_workflow

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.post("/evaluate")
def run_workflow(payload: dict):
    document_id = payload.get("document_id")
    extracted_text = payload.get("extracted_text")

    return evaluate_workflow(document_id, extracted_text)

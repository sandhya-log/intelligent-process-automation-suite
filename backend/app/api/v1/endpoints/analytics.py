from fastapi import APIRouter
from sqlalchemy import func
from backend.app.db.database import SessionLocal
from backend.app.db.models import Document

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/total-documents")
def total_documents():
    db = SessionLocal()
    count = db.query(func.count(Document.document_id)).scalar()
    db.close()
    return {"total_documents": count}


@router.get("/decision-breakdown")
def decision_breakdown():
    db = SessionLocal()
    results = (
        db.query(Document.decision, func.count(Document.decision))
        .group_by(Document.decision)
        .all()
    )
    db.close()

    return {
        "decisions": [
            {"decision": decision, "count": count}
            for decision, count in results
        ]
    }


@router.get("/system-summary")
def system_summary():
    db = SessionLocal()

    total = db.query(func.count(Document.document_id)).scalar()
    approved = db.query(Document).filter(Document.decision == "APPROVED").count()
    flagged = db.query(Document).filter(Document.decision == "FLAGGED").count()
    rejected = db.query(Document).filter(Document.decision == "REJECTED").count()

    db.close()

    return {
        "total": total,
        "approved": approved,
        "flagged": flagged,
        "rejected": rejected
    }

from app.db.database import SessionLocal
from app.db.models import Document


def answer_question(question: str) -> dict:
    db = SessionLocal()

    question_lower = question.lower()

    # Simple retrieval rules
    if "rejected" in question_lower:
        docs = db.query(Document).filter(Document.decision == "REJECTED").all()
        answer = f"There are {len(docs)} rejected documents."

    elif "approved" in question_lower:
        docs = db.query(Document).filter(Document.decision == "APPROVED").all()
        answer = f"There are {len(docs)} approved documents."

    elif "flagged" in question_lower:
        docs = db.query(Document).filter(Document.decision == "FLAGGED").all()
        answer = f"There are {len(docs)} flagged documents requiring review."

    else:
        answer = (
            "I can answer questions about document status such as "
            "approved, flagged, or rejected."
        )

    db.close()

    return {
        "question": question,
        "answer": answer
    }

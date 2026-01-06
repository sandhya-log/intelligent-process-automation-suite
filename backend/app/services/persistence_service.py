from backend.app.db.database import SessionLocal, engine
from backend.app.db.models import Document, Base

# Create tables
Base.metadata.create_all(bind=engine)


def save_document(
    document_id: str,
    filename: str,
    extracted_text: str,
    status: str,
    decision: str = None
):
    db = SessionLocal()
    try:
        doc = Document(
            document_id=document_id,
            filename=filename,
            extracted_text=extracted_text,
            status=status,
            decision=decision
        )
        db.add(doc)
        db.commit()
    finally:
        db.close()

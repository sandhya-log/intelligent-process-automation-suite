from sqlalchemy import Column, String, Text
from backend.app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    document_id = Column(String, primary_key=True, index=True)
    filename = Column(String)
    extracted_text = Column(Text)
    status = Column(String)
    decision = Column(String)

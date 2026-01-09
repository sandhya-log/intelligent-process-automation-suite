from fastapi import APIRouter
from app.services.chatbot_service import answer_question

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])


@router.post("/ask")
def ask_chatbot(payload: dict):
    question = payload.get("question")
    return answer_question(question)

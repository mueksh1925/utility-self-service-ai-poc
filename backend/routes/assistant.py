from fastapi import APIRouter
from pydantic import BaseModel

from ai.assistant_service import ask_assistant

router = APIRouter(
    prefix="/api/assistant",
    tags=["AI Assistant"]
)


class QuestionRequest(BaseModel):
    question: str


@router.post("/")
def assistant(request: QuestionRequest):
    return ask_assistant(request.question)
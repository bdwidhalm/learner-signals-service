from fastapi import APIRouter
from fastapi import status
from pydantic import BaseModel
from ..services import redpanda
from ..models.signal import Signal

# Define a Pydantic model for the request body
# class Signal(BaseModel):
#     question_id: str
#     question_text: str
#     question_category: str
#     question_difficulty: str
#     correct_answer: str
#     user_response: str
#     is_correct: bool
#     time_to_respond_seconds: float
#     response_changes_count: int

router = APIRouter()

@router.get("/signals/")
def get_signals():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]   

@router.post("/signals/", status_code=status.HTTP_201_CREATED)
def post_signal(signal: Signal):
    redpanda.publish(signal.toJSON())
    return signal
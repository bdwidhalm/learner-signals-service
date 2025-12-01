import json
from pydantic import BaseModel

# {
#   "question_id": "<string>",
#   "question_text": "<string>",
#   "question_category": "<string>",
#   "question_difficulty": "<easy|medium|hard>",
#   "correct_answer": "<string>",
#   "user_response": "<string>",
#   "is_correct": <true|false>,
#   "time_to_respond_seconds": <number>,
#   "response_changes_count": <number>
# }

class Signal(BaseModel):
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)
    
    question_id: str
    question_text: str
    question_category: str
    question_difficulty: str
    correct_answer: str
    user_response: str
    is_correct: bool
    time_to_respond_seconds: float
    response_changes_count: int
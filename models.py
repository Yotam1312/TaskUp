from pydantic import BaseModel
from typing import List

class LoginRequest(BaseModel):
    username: str
    password: str

class Assignment(BaseModel):
    course_name: str
    assignment_name: str
    upload_date: str
    due_date: str
    submitted: bool

class AssignmentsResponse(BaseModel):
    assignments: List[Assignment]
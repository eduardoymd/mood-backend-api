from pydantic import BaseModel
from typing import List
from app.models.tasks import Task

class OrganizeRequest(BaseModel):
    stress_score: int
    tasks: List[Task]
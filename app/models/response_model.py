from pydantic import BaseModel
from typing import List
from app.models.tasks import Task

class OrganizeResponse(BaseModel):
    ordered_tasks: List[Task]
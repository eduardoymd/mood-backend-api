from fastapi import APIRouter
from app.models.request_model import OrganizeRequest
from app.models.response_model import OrganizeResponse
from app.core.task_manager import TaskManager

router = APIRouter()
task_manager = TaskManager()

@router.post("/organizar-tarefas", response_model=OrganizeResponse)
def organizar_tarefas(req: OrganizeRequest):
    result = task_manager.organize(req.tasks, req.stress_score)
    return OrganizeResponse(ordered_tasks=result["ordered_tasks"])

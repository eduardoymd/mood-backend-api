from fastapi import FastAPI
from app.routes.tasks import router as tasks_router
app = FastAPI(
    title="Task Manger API",
    description="API para reorganização inteligente de tarefas baseada em IA",
    version="1.0.0",
)
app.include_router(tasks_router, prefix="/api", tags=["Task Organizer"])
@app.get("/")
def root():
    return {"status": "Task Manger API is running"}
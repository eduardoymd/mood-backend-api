from app.services.groq_service import GroqService

class TaskManager:
    def __init__(self):
        self.ai = GroqService(api_key="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")

    def organize(self, tasks, stress_score: int):
        return self.ai.organize_with_ai(tasks, stress_score)

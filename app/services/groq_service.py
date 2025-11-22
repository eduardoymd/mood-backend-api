import json
from groq import Groq

class GroqService:

    def __init__(self, api_key: str, model_name: str = "llama-3.1-8b-instant"):
        self.client = Groq(api_key=api_key)
        self.model_name = model_name

    def organize_with_ai(self, tasks, stress_score: int):

        tasks_text = "\n".join(
            [f"- Title: {t.title} | Description: {t.description} | Fixed: {t.fixed}"
             for t in tasks]
        )

        prompt = f"""
You are an AI engine for a Task Manager system that reorganizes user tasks according to well-being, mental load,
stress levels, emotional burden, physical effort, and semantic meaning.

Your mission is to help the user reduce cognitive stress by reordering tasks intelligently and consistently.

You MUST follow ALL rules exactly. No creativity outside the rules.

------------------------------------------------------------
### 1. OUTPUT FORMAT (MANDATORY)
Return ONLY valid JSON in this format:

{{
  "ordered_tasks": [
    {{ "title": "...", "description": "...", "fixed": true/false }}
  ]
}}

No explanations. No comments. No extra text.

------------------------------------------------------------
### 2. RULES (ABSOLUTE)
- DO NOT modify task titles
- DO NOT modify descriptions
- DO NOT modify fixed flags
- DO NOT add tasks
- DO NOT remove tasks
- DO NOT invent anything

You MUST output ALL tasks exactly as they came.

------------------------------------------------------------
### 3. FIXED TASK RULE
Tasks where fixed=true are **locked**.

You MUST:
1) Place ALL fixed tasks FIRST in the final list.
2) Keep their EXACT relative order from input.
3) Never reorder fixed tasks among themselves.

------------------------------------------------------------
### 4. SEMANTIC ANALYSIS RULE
For NON-fixed tasks ONLY:

Infer based on semantic meaning:
- emotional effort
- cognitive load
- physical effort
- urgency
- mental stress impact
- relaxation potential

------------------------------------------------------------
### 5. STRESS BEHAVIOR RULE (MANDATORY)

If stress_score >= 60:
    You MUST reorder NON-fixed tasks from LOW → HIGH impact:

    1) relaxing / simple / recovery tasks
    2) emotional moderate tasks
    3) heavy physical tasks
    4) heavy cognitive tasks  (last)

If stress_score < 60:
    Keep non-fixed tasks in original order.

------------------------------------------------------------
### USER STRESS
{stress_score}

### INPUT TASK LIST
{tasks_text}

Return ONLY the final JSON.
"""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You organize tasks following deterministic well-being rules."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except:
            return {"ordered_tasks": []}

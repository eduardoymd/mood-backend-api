# Mood Backend API
#### `Este projeto é um backend em Python (FastAPI) que reorganiza tarefas usando análise semântica e regras fixas, combinando lógica determinística com Inteligência Artificial (Groq).`
--- 
## Funcionalidades

### 1. Reorganização Inteligente de Tarefas

- Processa uma lista de tarefas enviadas pelo usuário.
- Reordena com base em regras fixas e análise semântica.
- Mantém todas as tarefas exatamente como recebidas (título, descrição e fixed).

### 2. Prioridade para Tarefas Fixas

- Tarefas com `fixed=true` sempre aparecem primeiro.
- A ordem entre elas é preservada exatamente como no input.
- Nunca são reordenadas entre si.

### 3. Análise Semântica das Tarefas

`A IA interpreta cada tarefa considerando:`

- nível de esforço cognitivo
- esforço físico
- carga emocional
- urgência
- potencial relaxante
- impacto psicológico
- nível de complexidade
- intensidade mental ou física

---
### 📌 Como Usar

#### 1. Instale todas as dependências
`pip install fastapi uvicorn groq python-dotenv`

#### 2. Configure sua chave de API do Groq
`GROQ_API_KEY=SUA_CHAVE_AQUI`

#### 3. Rode o servidor
`uvicorn app.main:app --reload`

--- 
### Integrantes

- **Eduardo Eiki - RM 554921**
- **Nicollas Frei - RM 557647**

- **Heitor Duarte - RM 558208**

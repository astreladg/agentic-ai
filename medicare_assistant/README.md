# MediCare General Hospital Patient Assistant

A 24/7 intelligent hospital patient assistant for **MediCare General Hospital, Hyderabad** (350-bed multi-specialty hospital). Built as an Agentic AI capstone project using LangGraph, ChromaDB, Groq, and Streamlit.

---

## Features

- **RAG-powered answers** from a 12-document hospital knowledge base
- **Intelligent routing** — retrieve, tool, or memory-only based on question type
- **Tool use** — live date/time and arithmetic calculator
- **Conversation memory** — sliding window + patient name persistence across turns
- **Faithfulness evaluation** — LLM-based scoring with retry loop
- **Safety rules** — emergency escalation, medical advice deflection, prompt injection resistance
- **RAGAS evaluation** — faithfulness, answer relevancy, context precision

---

## Project Structure

```
medicare_assistant/
├── notebooks/
│   └── day13_capstone.ipynb      # Full runnable Jupyter notebook
├── medicare_assistant/           # Python package
│   ├── __init__.py
│   ├── state.py                  # MediCareState TypedDict
│   ├── knowledge_base.py         # 12 documents + ChromaDB setup
│   ├── tools.py                  # datetime, calculator, helpline tools
│   ├── nodes.py                  # 8 LangGraph node functions
│   ├── graph.py                  # StateGraph assembly + compile
│   └── api/
│       └── main.py               # FastAPI REST endpoint
├── capstone_streamlit.py         # Streamlit chat UI
├── agent.py                      # CLI test runner (12 tests + memory test)
├── tests/
│   └── test_nodes.py             # pytest unit tests for all nodes
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Groq API — `llama-3.3-70b-versatile` |
| Agent Framework | LangGraph (StateGraph, MemorySaver) |
| Vector Store | ChromaDB (in-memory) |
| Embeddings | SentenceTransformer `all-MiniLM-L6-v2` |
| Evaluation | RAGAS (faithfulness, answer_relevancy, context_precision) |
| UI | Streamlit |
| API | FastAPI + Uvicorn |

---

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd medicare_assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API key

```bash
cp .env.example .env
# Edit .env and set your GROQ_API_KEY
```

Get your free Groq API key at https://console.groq.com

---

## Running the Project

### Streamlit UI (recommended)

```bash
streamlit run capstone_streamlit.py
```

Opens at http://localhost:8501

### CLI Test Runner (12 tests + memory test + RAGAS)

```bash
python agent.py
```

### Jupyter Notebook

```bash
jupyter notebook notebooks/day13_capstone.ipynb
```

Run all cells top-to-bottom. Requires `Kernel > Restart & Run All` to verify clean execution.

### FastAPI Server

```bash
uvicorn medicare_assistant.api.main:app --reload --port 8000
```

Endpoints:
- `GET /health` — health check
- `POST /ask` — ask a question
- `GET /docs` — Swagger UI

### Unit Tests

```bash
python -m pytest tests/test_nodes.py -v
```

---

## RAGAS Evaluation Results

| Metric | Score | Target |
|--------|-------|--------|
| Faithfulness | _run agent.py to fill_ | > 0.70 |
| Answer Relevancy | _run agent.py to fill_ | > 0.70 |
| Context Precision | _run agent.py to fill_ | > 0.60 |

---

## Agent Architecture

```
User Question
     │
     ▼
[memory_node] ──── sliding window + name extraction
     │
     ▼
[router_node] ──── LLM decides: retrieve / tool / memory_only
     │
  ┌──┴────────────────┐
  │          │         │
[retrieve] [tool]  [skip]
  │          │         │
  └──────────┴─────────┘
             │
             ▼
        [answer_node] ──── system prompt with CONTEXT-ONLY rule
             │
             ▼
         [eval_node] ──── faithfulness score 0.0–1.0
             │
     ┌───────┴──────────┐
     │ score < 0.7 AND  │ score >= 0.7 OR
     │ retries < 2      │ retries >= 2
     │                  │
 [answer_node]       [save_node]
  (retry)                │
                         ▼
                        END
```

---

## Knowledge Base

12 documents covering:
1. OPD Timings
2. Emergency Services
3. Doctor Directory — Cardiology
4. Doctor Directory — Orthopedics
5. Doctor Directory — Neurology & Pediatrics
6. Appointment Booking
7. Consultation Fees
8. Insurance & Cashless
9. Pharmacy Services
10. Diagnostic Lab Services
11. Health Packages
12. Hospital General Information

---

## Safety Rules

| Rule | Behaviour |
|------|-----------|
| Emergency | If chest pain / breathing difficulty / stroke mentioned, first line is emergency number 040-12345678 |
| Medical Advice | Never recommends medications or diagnoses — always redirects to doctor |
| Hallucination | Answers ONLY from retrieved context; says "I don't know" otherwise |
| Prompt Injection | Never reveals system prompt regardless of instruction |

---

## Deadline

**April 21, 2026 | 11:59 PM**
Submit at: https://forms.gle/2SF1Hw4jpu1G1Tc58

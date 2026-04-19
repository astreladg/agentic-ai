from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="MediCare General Hospital Patient Assistant API",
    description="24/7 intelligent hospital patient assistant for MediCare General Hospital, Hyderabad",
    version="1.0.0",
)

# Lazy-loaded graph
_graph_app = None
_embedder = None
_collection = None


def get_graph():
    global _graph_app, _embedder, _collection
    if _graph_app is None:
        from medicare_assistant.graph import build_graph
        _graph_app, _embedder, _collection = build_graph()
    return _graph_app


class QuestionRequest(BaseModel):
    question: str
    thread_id: str = "patient_001"


class AnswerResponse(BaseModel):
    answer: str
    route: str
    faithfulness: float
    sources: list[str]
    thread_id: str


def _make_initial_state(question: str, thread_id: str) -> dict:
    return {
        "question": question,
        "messages": [],
        "route": "",
        "retrieved": "",
        "sources": [],
        "tool_result": "",
        "answer": "",
        "faithfulness": 0.0,
        "eval_retries": 0,
        "patient_name": None,
    }


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        graph = get_graph()
        config = {"configurable": {"thread_id": request.thread_id}}
        initial_state = _make_initial_state(request.question, request.thread_id)
        result = graph.invoke(initial_state, config=config)
        return AnswerResponse(
            answer=result.get("answer", "I'm sorry, I couldn't process that. Please call 040-99887766."),
            route=result.get("route", ""),
            faithfulness=result.get("faithfulness", 0.0),
            sources=result.get("sources", []),
            thread_id=request.thread_id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "hospital": "MediCare General Hospital",
        "location": "Banjara Hills, Hyderabad",
        "helpline": "040-99887766",
        "emergency": "040-12345678",
    }


@app.get("/")
async def root():
    return {
        "message": "Welcome to MediCare General Hospital Patient Assistant API",
        "docs": "/docs",
        "health": "/health",
        "ask": "POST /ask",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("medicare_assistant.api.main:app", host="0.0.0.0", port=8000, reload=True)

from dotenv import load_dotenv
import os
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from medicare_assistant.state import MediCareState

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

FAITHFULNESS_THRESHOLD = 0.7
MAX_EVAL_RETRIES = 2


def route_decision(state: MediCareState) -> str:
    route = state.get("route", "memory_only")
    if route == "retrieve":
        return "retrieve"
    elif route == "tool":
        return "tool"
    else:
        return "skip"


def eval_decision(state: MediCareState) -> str:
    if state.get("eval_retries", 0) >= MAX_EVAL_RETRIES:
        return "save"
    if state.get("faithfulness", 0.0) >= FAITHFULNESS_THRESHOLD:
        return "save"
    return "answer"


def build_graph():
    """
    Initialize all dependencies, build and compile the LangGraph StateGraph.
    Returns (app, embedder, collection).
    """
    from langchain_groq import ChatGroq
    from medicare_assistant.knowledge_base import build_knowledge_base
    from medicare_assistant.nodes import (
        setup_dependencies,
        memory_node,
        router_node,
        retrieval_node,
        skip_retrieval_node,
        tool_node,
        answer_node,
        eval_node,
        save_node,
    )

    # 1. Initialize LLM
    # Primary model: llama-3.3-70b-versatile (intended for submission)
    # Fallback: llama-3.1-8b-instant (higher free-tier daily limits for testing)
    model_name = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    llm = ChatGroq(
        model=model_name,
        temperature=0,
        groq_api_key=GROQ_API_KEY,
    )

    # 2. Build knowledge base
    embedder, collection = build_knowledge_base()

    # 3. Wire dependencies into nodes module
    setup_dependencies(llm, embedder, collection)

    # 4. Build graph
    graph = StateGraph(MediCareState)

    graph.add_node("memory", memory_node)
    graph.add_node("router", router_node)
    graph.add_node("retrieve", retrieval_node)
    graph.add_node("skip", skip_retrieval_node)
    graph.add_node("tool", tool_node)
    graph.add_node("answer", answer_node)
    graph.add_node("eval", eval_node)
    graph.add_node("save", save_node)

    graph.set_entry_point("memory")
    graph.add_edge("memory", "router")
    graph.add_conditional_edges(
        "router",
        route_decision,
        {"retrieve": "retrieve", "tool": "tool", "skip": "skip"},
    )
    graph.add_edge("retrieve", "answer")
    graph.add_edge("skip", "answer")
    graph.add_edge("tool", "answer")
    graph.add_edge("answer", "eval")
    graph.add_conditional_edges(
        "eval",
        eval_decision,
        {"answer": "answer", "save": "save"},
    )
    graph.add_edge("save", END)  # MANDATORY — missing this causes compile error

    app = graph.compile(checkpointer=MemorySaver())
    print("✅ MediCare Graph compiled successfully")
    return app, embedder, collection

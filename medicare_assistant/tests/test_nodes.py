"""
Unit tests for MediCare assistant node functions.
Each node is tested in isolation with a mock state dict.
Run: python -m pytest tests/test_nodes.py -v
"""
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_state(**overrides) -> dict:
    """Return a fully populated mock MediCareState."""
    base = {
        "question": "What are the OPD timings?",
        "messages": [],
        "route": "retrieve",
        "retrieved": "[OPD Timings]: Monday to Saturday 8am-8pm",
        "sources": ["OPD Timings"],
        "tool_result": "",
        "answer": "OPD timings are Monday to Saturday 8am to 8pm.",
        "faithfulness": 0.9,
        "eval_retries": 0,
        "patient_name": None,
    }
    base.update(overrides)
    return base


@pytest.fixture(scope="module")
def deps():
    """Build real LLM + KB for integration-style tests."""
    from langchain_groq import ChatGroq
    from medicare_assistant.knowledge_base import build_knowledge_base
    from medicare_assistant.nodes import setup_dependencies

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY"),
    )
    embedder, collection = build_knowledge_base()
    setup_dependencies(llm, embedder, collection)
    return llm, embedder, collection


# ---------------------------------------------------------------------------
# memory_node
# ---------------------------------------------------------------------------

def test_memory_node_appends_message():
    from medicare_assistant.nodes import memory_node
    state = _make_state(question="Hello", messages=[], patient_name=None)
    result = memory_node(state)
    assert result["messages"][-1]["role"] == "user"
    assert result["messages"][-1]["content"] == "Hello"


def test_memory_node_sliding_window():
    from medicare_assistant.nodes import memory_node
    messages = [{"role": "user", "content": f"msg {i}"} for i in range(10)]
    state = _make_state(question="new question", messages=messages)
    result = memory_node(state)
    assert len(result["messages"]) <= 6


def test_memory_node_extracts_name():
    from medicare_assistant.nodes import memory_node
    state = _make_state(question="My name is Priya Sharma", messages=[], patient_name=None)
    result = memory_node(state)
    assert result["patient_name"] == "Priya Sharma"


# ---------------------------------------------------------------------------
# router_node
# ---------------------------------------------------------------------------

def test_router_returns_valid_route(deps):
    from medicare_assistant.nodes import router_node
    for question, expected in [
        ("What are the OPD timings?", "retrieve"),
        ("What is today's date?", "tool"),
        ("Hello!", "memory_only"),
    ]:
        state = _make_state(question=question)
        result = router_node(state)
        assert result["route"] in ("retrieve", "tool", "memory_only"), \
            f"Invalid route '{result['route']}' for question: {question}"


# ---------------------------------------------------------------------------
# retrieval_node
# ---------------------------------------------------------------------------

def test_retrieval_node_returns_context(deps):
    from medicare_assistant.nodes import retrieval_node
    state = _make_state(question="What are the cardiology OPD timings?")
    result = retrieval_node(state)
    assert len(result["retrieved"]) > 0
    assert len(result["sources"]) > 0


# ---------------------------------------------------------------------------
# skip_retrieval_node
# ---------------------------------------------------------------------------

def test_skip_retrieval_node_returns_empty():
    from medicare_assistant.nodes import skip_retrieval_node
    state = _make_state(retrieved="some context", sources=["Some Topic"])
    result = skip_retrieval_node(state)
    assert result["retrieved"] == ""
    assert result["sources"] == []


def test_skip_retrieval_never_returns_empty_dict():
    from medicare_assistant.nodes import skip_retrieval_node
    state = _make_state()
    result = skip_retrieval_node(state)
    assert "retrieved" in result
    assert "sources" in result


# ---------------------------------------------------------------------------
# tool_node
# ---------------------------------------------------------------------------

def test_tool_node_datetime(deps):
    from medicare_assistant.nodes import tool_node
    state = _make_state(question="What is today's date?")
    result = tool_node(state)
    assert "date" in result["tool_result"].lower() or "current" in result["tool_result"].lower()


def test_tool_node_calculate(deps):
    from medicare_assistant.nodes import tool_node
    state = _make_state(question="What is 500 plus 800?")
    result = tool_node(state)
    assert "1300" in result["tool_result"]


def test_tool_node_no_exception(deps):
    from medicare_assistant.nodes import tool_node
    # Malformed expression should return error string, not raise
    state = _make_state(question="What is abc divided by xyz?")
    result = tool_node(state)
    assert isinstance(result["tool_result"], str)


# ---------------------------------------------------------------------------
# answer_node
# ---------------------------------------------------------------------------

def test_answer_node_returns_string(deps):
    from medicare_assistant.nodes import answer_node
    state = _make_state(
        question="What are the OPD timings?",
        retrieved="[OPD Timings]: Monday to Saturday 8am to 8pm.",
        tool_result="",
    )
    result = answer_node(state)
    assert isinstance(result["answer"], str)
    assert len(result["answer"]) > 0


def test_answer_node_addresses_patient_by_name(deps):
    from medicare_assistant.nodes import answer_node
    state = _make_state(
        question="What are OPD timings?",
        retrieved="[OPD Timings]: Monday to Saturday 8am-8pm.",
        patient_name="Rahul",
    )
    result = answer_node(state)
    assert "rahul" in result["answer"].lower()


# ---------------------------------------------------------------------------
# eval_node
# ---------------------------------------------------------------------------

def test_eval_node_scores_retrieved(deps):
    from medicare_assistant.nodes import eval_node
    state = _make_state(retrieved="[OPD Timings]: 8am-8pm", answer="OPD is 8am to 8pm.")
    result = eval_node(state)
    assert 0.0 <= result["faithfulness"] <= 1.0
    assert result["eval_retries"] == 1


def test_eval_node_skips_when_no_retrieved(deps):
    from medicare_assistant.nodes import eval_node
    state = _make_state(retrieved="", answer="Hi there!", eval_retries=0)
    result = eval_node(state)
    assert result["faithfulness"] == 1.0


# ---------------------------------------------------------------------------
# save_node
# ---------------------------------------------------------------------------

def test_save_node_appends_assistant_message():
    from medicare_assistant.nodes import save_node
    state = _make_state(
        messages=[{"role": "user", "content": "Hello"}],
        answer="The OPD timings are 8am to 8pm.",
    )
    result = save_node(state)
    assert result["messages"][-1]["role"] == "assistant"
    assert result["messages"][-1]["content"] == "The OPD timings are 8am to 8pm."


# ---------------------------------------------------------------------------
# Tools (standalone)
# ---------------------------------------------------------------------------

def test_get_current_datetime():
    from medicare_assistant.tools import get_current_datetime
    result = get_current_datetime()
    assert "date" in result.lower() or "current" in result.lower()


def test_calculate_basic():
    from medicare_assistant.tools import calculate
    result = calculate("500 + 800")
    assert "1300" in result


def test_calculate_error_safe():
    from medicare_assistant.tools import calculate
    result = calculate("not a number!!!!")
    assert isinstance(result, str)  # must not raise


def test_get_helpline():
    from medicare_assistant.tools import get_helpline
    result = get_helpline()
    assert "040-99887766" in result
    assert "040-12345678" in result

from typing import TypedDict, List, Optional


class MediCareState(TypedDict):
    question: str
    messages: List[dict]
    route: str                    # "retrieve" | "tool" | "memory_only"
    retrieved: str
    sources: List[str]
    tool_result: str
    answer: str
    faithfulness: float
    eval_retries: int
    patient_name: Optional[str]

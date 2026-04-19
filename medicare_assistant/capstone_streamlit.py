"""
MediCare General Hospital — Patient Assistant UI (v3.0)
Premium dark-mode Streamlit interface with full LangGraph backend.
"""
import streamlit as st
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ── Page config MUST be first Streamlit call ──────────────────────────────────
st.set_page_config(
    page_title="MediCare Patient Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── BASE ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}
.stApp {
    background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 50%, #0a0f1e 100%) !important;
}
#MainMenu, footer { visibility: hidden; }
/* Keep header visible so the sidebar toggle arrow is clickable, but transparent */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: auto !important;
}
/* Make the sidebar collapse/expand control always visible and styled */
button[data-testid="stSidebarCollapseButton"],
button[data-testid="collapsedControl"] {
    color: #e2e8f0 !important;
    background: rgba(30, 64, 175, 0.6) !important;
    border-radius: 8px !important;
    visibility: visible !important;
    display: flex !important;
}
.block-container {
    padding: 1.5rem 2rem 4rem !important;
    max-width: 960px !important;
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: rgba(10, 15, 30, 0.95) !important;
    border-right: 1px solid rgba(99, 179, 237, 0.12) !important;
    min-width: 280px !important;
    max-width: 280px !important;
}
section[data-testid="stSidebar"] > div {
    background: transparent !important;
    padding: 1rem !important;
}
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div {
    color: #e2e8f0 !important;
}
section[data-testid="stSidebar"] hr {
    border-color: rgba(99, 179, 237, 0.15) !important;
    margin: 16px 0 !important;
}

/* Sidebar new-conversation button */
section[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(135deg, #1e40af, #1d4ed8) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    padding: 0.6rem 1rem !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 14px rgba(29, 78, 216, 0.4) !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: linear-gradient(135deg, #2563eb, #3b82f6) !important;
    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5) !important;
    transform: translateY(-1px) !important;
}

/* ── CONTACT CARDS (sidebar) ── */
.contact-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 12px 14px;
    margin: 8px 0;
}
.contact-card.emergency {
    background: rgba(220, 38, 38, 0.12);
    border-color: rgba(220, 38, 38, 0.3);
}
.contact-card .contact-label {
    font-size: 0.72rem !important;
    color: #94a3b8 !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
    margin-bottom: 2px;
}
.contact-card.emergency .contact-label { color: #fca5a5 !important; }
.contact-card .contact-number {
    font-size: 1rem !important;
    font-weight: 700 !important;
    color: #f8fafc !important;
}

/* ── HEADER BANNER ── */
.header-banner {
    background: rgba(14, 21, 47, 0.8);
    border: 1px solid rgba(99, 179, 237, 0.15);
    border-radius: 20px;
    padding: 24px 32px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
}
.header-icon { font-size: 52px; line-height: 1; }
.header-title {
    font-size: 1.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, #60a5fa, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.2;
}
.header-sub {
    color: #94a3b8;
    font-size: 0.9rem;
    margin: 4px 0 0;
}
.online-badge {
    margin-left: auto;
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 20px;
    padding: 6px 16px;
    color: #34d399;
    font-size: 0.82rem;
    font-weight: 600;
    white-space: nowrap;
}

/* ── QUICK QUESTION CHIPS ── */
.chip-section-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 10px;
    margin-top: 4px;
}

/* Override ALL stButton styles for chips */
.stButton > button {
    background: rgba(30, 41, 60, 0.7) !important;
    color: #cbd5e1 !important;
    border: 1px solid rgba(148, 163, 184, 0.15) !important;
    border-radius: 8px !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    padding: 6px 10px !important;
    transition: all 0.2s ease !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    width: 100% !important;
    line-height: 1.2 !important;
    min-height: 36px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.stButton > button:hover {
    background: rgba(59, 130, 246, 0.2) !important;
    color: #93c5fd !important;
    border-color: rgba(59, 130, 246, 0.4) !important;
    transform: translateY(-1px) !important;
}

/* ── WELCOME CARD ── */
.welcome-card {
    background: rgba(14, 21, 47, 0.7);
    border: 1px solid rgba(99, 179, 237, 0.12);
    border-left: 4px solid #3b82f6;
    border-radius: 16px;
    padding: 28px 32px;
    margin: 16px 0 24px;
    color: #e2e8f0;
}
.welcome-card h3 {
    color: #f1f5f9;
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0 0 10px;
}
.welcome-card p {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.7;
    margin: 0 0 16px;
}
.emergency-alert {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(220, 38, 38, 0.12);
    border: 1px solid rgba(220, 38, 38, 0.3);
    border-radius: 8px;
    padding: 8px 14px;
    color: #fca5a5;
    font-size: 0.85rem;
    font-weight: 600;
}

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] {
    background: transparent !important;
    padding: 8px 0 !important;
    border-radius: 0 !important;
    border: none !important;
}

/* Text inside all messages — must be white on dark background */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] strong,
[data-testid="stChatMessage"] em {
    color: #e2e8f0 !important;
    font-size: 0.95rem !important;
    line-height: 1.65 !important;
}

/* User message bubble */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background: rgba(59, 130, 246, 0.08) !important;
    border: 1px solid rgba(59, 130, 246, 0.18) !important;
    border-radius: 14px !important;
    padding: 14px 18px !important;
    margin: 6px 0 !important;
}

/* Assistant message bubble */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
    background: rgba(20, 30, 55, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 14px !important;
    padding: 14px 18px !important;
    margin: 6px 0 !important;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInput"] > div {
    background: rgba(14, 21, 47, 0.9) !important;
    border: 1px solid rgba(99, 179, 237, 0.2) !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.25s ease !important;
}
[data-testid="stChatInput"] > div:focus-within {
    border-color: rgba(59, 130, 246, 0.5) !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1), 0 4px 20px rgba(0, 0, 0, 0.3) !important;
}
[data-testid="stChatInput"] textarea {
    color: #f1f5f9 !important;
    font-size: 0.95rem !important;
    font-weight: 400 !important;
    caret-color: #60a5fa !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #475569 !important;
}

/* ── SOURCES EXPANDER ── */
[data-testid="stExpander"] {
    background: rgba(15, 23, 42, 0.5) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 10px !important;
}
[data-testid="stExpander"] summary {
    color: #64748b !important;
    font-size: 0.82rem !important;
}

/* ── DIVIDER ── */
hr { border-color: rgba(255,255,255,0.06) !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(148,163,184,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(148,163,184,0.4); }
</style>
""", unsafe_allow_html=True)


# ── Cached agent (all heavy init inside) ──────────────────────────────────────
@st.cache_resource
def load_agent():
    """Load LLM, knowledge base, and compile graph. Cached across sessions."""
    from dotenv import load_dotenv
    load_dotenv()

    import os as _os
    from langchain_groq import ChatGroq
    from medicare_assistant.knowledge_base import build_knowledge_base
    from medicare_assistant.nodes import (
        setup_dependencies,
        memory_node, router_node, retrieval_node, skip_retrieval_node,
        tool_node, answer_node, eval_node, save_node,
    )
    from medicare_assistant.graph import route_decision, eval_decision
    from langgraph.graph import StateGraph, END
    from langgraph.checkpoint.memory import MemorySaver
    from medicare_assistant.state import MediCareState

    # Read from st.secrets first (Streamlit Cloud), then fall back to env vars (.env local)
    def _cfg(key, default=None):
        try:
            if key in st.secrets:
                return st.secrets[key]
        except Exception:
            pass
        return _os.getenv(key, default)

    api_key = _cfg("GROQ_API_KEY")
    if not api_key:
        st.error("❌ GROQ_API_KEY not configured. Add it in Streamlit → Settings → Secrets.")
        st.stop()

    llm = ChatGroq(
        model=_cfg("GROQ_MODEL", "llama-3.1-8b-instant"),
        temperature=0,
        groq_api_key=api_key,
    )
    embedder, collection = build_knowledge_base()
    setup_dependencies(llm, embedder, collection)

    g = StateGraph(MediCareState)
    for name, fn in [
        ("memory",   memory_node),
        ("router",   router_node),
        ("retrieve", retrieval_node),
        ("skip",     skip_retrieval_node),
        ("tool",     tool_node),
        ("answer",   answer_node),
        ("eval",     eval_node),
        ("save",     save_node),
    ]:
        g.add_node(name, fn)

    g.set_entry_point("memory")
    g.add_edge("memory", "router")
    g.add_conditional_edges("router", route_decision,
        {"retrieve": "retrieve", "tool": "tool", "skip": "skip"})
    for src in ("retrieve", "skip", "tool"):
        g.add_edge(src, "answer")
    g.add_edge("answer", "eval")
    g.add_conditional_edges("eval", eval_decision,
        {"answer": "answer", "save": "save"})
    g.add_edge("save", END)

    app = g.compile(checkpointer=MemorySaver())
    return app, embedder, collection


def get_answer(prompt: str, thread_id: str, language: str = "English") -> tuple[str, list]:
    """Invoke the graph and return (answer, sources)."""
    app, _, _ = load_agent()
    cfg = {"configurable": {"thread_id": thread_id}}

    try:
        snap = app.get_state(cfg)
        saved = snap.values if snap and snap.values else {}
    except Exception:
        saved = {}

    # Prepend explicit language instruction to the question for guaranteed compliance
    lang_prefix = (
        f"[REPLY IN {language.upper()} LANGUAGE ONLY] "
        if language != "English"
        else ""
    )
    augmented_prompt = lang_prefix + prompt

    result = app.invoke({
        "question":     augmented_prompt,
        "messages":     saved.get("messages", []),
        "route":        "",
        "retrieved":    "",
        "sources":      [],
        "tool_result":  "",
        "answer":       "",
        "faithfulness": 0.0,
        "eval_retries": 2,   # Skip faithfulness eval in UI — saves one LLM round-trip
        "patient_name": saved.get("patient_name", None),
    }, config=cfg)

    answer = result.get("answer",
        "I'm sorry, I couldn't process that. Please call **040-99887766**.")
    sources = result.get("sources", [])
    return answer, sources


# ── Session state init ──────────────────────────────────────────────────────────────
if "messages"       not in st.session_state:
    st.session_state.messages = []
if "thread_id"      not in st.session_state:
    st.session_state.thread_id = f"patient_{int(time.time())}"
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None
if "language"       not in st.session_state:
    st.session_state.language = "English"
if "is_processing"  not in st.session_state:
    st.session_state.is_processing = False


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    # Hospital logo & name
    st.markdown("""
    <div style="text-align:center; padding: 12px 0 20px;">
        <div style="font-size:56px;">🏥</div>
        <div style="font-weight:700; font-size:1.15rem; color:#f1f5f9; margin-top:10px;">
            MediCare General
        </div>
        <div style="font-size:0.8rem; color:#64748b; margin-top:3px;">
            Banjara Hills · Hyderabad
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Contact cards
    contacts = [
        ("📞", "Helpline",       "040-99887766", False),
        ("🚨", "Emergency 24/7", "040-12345678", True),
        ("💊", "Pharmacy",       "040-99887755", False),
        ("🔬", "Lab",            "040-99887744", False),
    ]
    for icon, label, number, is_emergency in contacts:
        cls = "contact-card emergency" if is_emergency else "contact-card"
        st.markdown(f"""
        <div class="{cls}">
            <div class="contact-label">{icon} {label}</div>
            <div class="contact-number">{number}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Services list
    st.markdown("""
    <div style="font-size:0.8rem; color:#64748b; font-weight:600; text-transform:uppercase;
                letter-spacing:0.08em; margin-bottom:10px;">I can help with</div>
    <div style="font-size:0.88rem; color:#94a3b8; line-height:2.0;">
        🩺 OPD timings &amp; doctors<br>
        💰 Consultation fees<br>
        📅 Appointment booking<br>
        🛡️ Insurance &amp; cashless<br>
        💊 Pharmacy services<br>
        🔬 Lab &amp; diagnostics<br>
        📦 Health packages<br>
        🚑 Emergency services
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Language Selector ──
    LANGUAGES = {
        "🇬🇧 English":  "English",
        "🇮🇳 Hindi (हिंदी)": "Hindi",
        "🇮🇳 Telugu (తెలుగు)": "Telugu",
        "🇮🇳 Tamil (தமிழ்)": "Tamil",
        "🇮🇳 Kannada (ಕನ್ನಡ)": "Kannada",
        "🇮🇳 Urdu (اردو)": "Urdu",
        "🇮🇳 Bengali (বাংলা)": "Bengali",
        "🇮🇳 Marathi (मराठी)": "Marathi",
    }
    st.markdown("""
    <div style="font-size:0.8rem; color:#64748b; font-weight:600; text-transform:uppercase;
                letter-spacing:0.08em; margin-bottom:8px;">🌐 Language / भाषा</div>
    """, unsafe_allow_html=True)
    selected_display = st.selectbox(
        label="language_selector",
        options=list(LANGUAGES.keys()),
        index=list(LANGUAGES.values()).index(st.session_state.language)
              if st.session_state.language in LANGUAGES.values() else 0,
        label_visibility="collapsed",
        key="lang_select",
    )
    st.session_state.language = LANGUAGES[selected_display]

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("🔄  New Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.thread_id = f"patient_{int(time.time())}"
        st.session_state.pending_prompt = None
        st.rerun()

    st.markdown("""
    <div style="text-align:center; font-size:0.75rem; color:#334155;
                margin-top:24px; line-height:1.8;">
        MediCare Assistant v3.0<br>
        Powered by LangGraph &amp; Groq
    </div>
    """, unsafe_allow_html=True)


# ── MAIN CONTENT ──────────────────────────────────────────────────────────────

# Header banner
st.markdown("""
<div class="header-banner">
    <div class="header-icon">🏥</div>
    <div>
        <div class="header-title">MediCare Patient Assistant</div>
        <div class="header-sub">Compassionate Care · Advanced Technology · Banjara Hills, Hyderabad</div>
    </div>
    <div class="online-badge">🟢 Online 24/7</div>
</div>
""", unsafe_allow_html=True)

# ── Quick question chips ──────────────────────────────────────────────────────
QUICK_QUESTIONS = [
    ("🕐", "OPD Timings",       "What are the OPD timings for all departments?"),
    ("💰", "Doctor Fees",       "How much does a specialist consultation cost?"),
    ("📅", "Book Appointment",  "How do I book an appointment at MediCare?"),
    ("🛡️", "Insurance",         "Does MediCare accept Star Health insurance?"),
    ("🔬", "Lab Timings",       "What are the lab timings and home collection details?"),
    ("📦", "Health Packages",   "What health packages are available and what do they cost?"),
    ("💊", "Pharmacy",          "What are the pharmacy timings and services?"),
    ("🚨", "Emergency",         "What is the emergency contact number?"),
]

st.markdown('<div class="chip-section-label">Quick questions</div>', unsafe_allow_html=True)

# Render chips in 2 rows of 4
row1 = QUICK_QUESTIONS[:4]
row2 = QUICK_QUESTIONS[4:]

cols1 = st.columns(4)
for i, (icon, label, question) in enumerate(row1):
    with cols1[i]:
        if st.button(f"{icon} {label}", key=f"quick_{i}",
                     disabled=st.session_state.is_processing):
            if not st.session_state.is_processing:
                st.session_state.pending_prompt = question

cols2 = st.columns(4)
for i, (icon, label, question) in enumerate(row2):
    with cols2[i]:
        if st.button(f"{icon} {label}", key=f"quick_{i+4}",
                     disabled=st.session_state.is_processing):
            if not st.session_state.is_processing:
                st.session_state.pending_prompt = question

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# ── Welcome card (only on fresh start) ───────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-card">
        <h3>👋 Hello! I'm your MediCare Patient Assistant</h3>
        <p>
            I can help you with <strong>OPD timings</strong>, <strong>doctor availability</strong>,
            <strong>consultation fees</strong>, <strong>insurance &amp; cashless facilities</strong>,
            <strong>pharmacy</strong>, <strong>lab services</strong>, and <strong>health packages</strong>.<br>
            Select a quick question above or type your query below.
        </p>
        <div class="emergency-alert">
            🚨 For emergencies, call <strong>040-12345678</strong> immediately.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Chat history ──────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ── Process a turn ──────────────────────────────────────────────────────────────
def run_turn(prompt: str):
    """Append user message, call agent, display and store assistant reply."""
    # Guard: never run if already processing
    if st.session_state.is_processing:
        return

    st.session_state.is_processing = True

    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt, "sources": []})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown(
            "<span style='color:#475569;font-size:0.9rem'>Thinking…</span>",
            unsafe_allow_html=True,
        )
        try:
            answer, sources = get_answer(prompt, st.session_state.thread_id, st.session_state.language)
        except Exception as exc:
            err_str = str(exc)
            if "429" in err_str or "rate" in err_str.lower():
                answer = (
                    "⚠️ I'm receiving too many requests right now. "
                    "Please wait a moment and try again, or call **040-99887766** for immediate assistance."
                )
            else:
                answer = (
                    "⚠️ I encountered a technical issue. "
                    "Please call **040-99887766** for immediate assistance."
                )
            sources = []

        placeholder.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": [],
    })

    # Release the lock
    st.session_state.is_processing = False


# ── Handle pending quick-chip trigger ───────────────────────────────────────────────
if st.session_state.pending_prompt and not st.session_state.is_processing:
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None
    run_turn(prompt)
    st.rerun()

# ── Chat input ────────────────────────────────────────────────────────────────
if user_input := st.chat_input("Ask me anything about MediCare Hospital…"):
    run_turn(user_input)

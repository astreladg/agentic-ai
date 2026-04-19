"""Generate MediCare Capstone Project Report PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUT = "MediCare_Capstone_Report.pdf"

NAVY = colors.HexColor("#0f2d6b")
BLUE = colors.HexColor("#1565c0")
LIGHT = colors.HexColor("#e8f0fe")
GREY = colors.HexColor("#64748b")
TEAL = colors.HexColor("#0d9488")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBox", fontName="Helvetica-Bold",
    fontSize=22, textColor=colors.white, alignment=TA_CENTER, leading=28))
styles.add(ParagraphStyle(name="SubtitleBox", fontName="Helvetica",
    fontSize=12, textColor=colors.whitesmoke, alignment=TA_CENTER, leading=16))
styles.add(ParagraphStyle(name="H1", fontName="Helvetica-Bold",
    fontSize=13, textColor=BLUE, spaceBefore=14, spaceAfter=6, leading=16))
styles.add(ParagraphStyle(name="H2", fontName="Helvetica-Bold",
    fontSize=11, textColor=NAVY, spaceBefore=6, spaceAfter=3, leading=14))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica",
    fontSize=10, textColor=colors.HexColor("#1e293b"),
    alignment=TA_JUSTIFY, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name="Bul", fontName="Helvetica",
    fontSize=10, textColor=colors.HexColor("#1e293b"),
    leftIndent=14, bulletIndent=4, leading=14, spaceAfter=3))
styles.add(ParagraphStyle(name="Caption", fontName="Helvetica-Oblique",
    fontSize=9, textColor=GREY, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name="Footer", fontName="Helvetica",
    fontSize=8, textColor=GREY, alignment=TA_CENTER))


def section(title):
    t = Table([[Paragraph(title, styles["H1"])]], colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LIGHT),
        ("LINEBELOW", (0,0), (-1,-1), 1.2, BLUE),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t


def title_block():
    data = [
        [Paragraph("MediCare Patient Assistant", styles["TitleBox"])],
        [Paragraph("An Agentic AI Hospital Helpdesk using LangGraph, ChromaDB & Groq", styles["SubtitleBox"])],
        [Spacer(1, 6)],
        [Paragraph("Capstone Project Report", styles["SubtitleBox"])],
    ]
    t = Table(data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("TOPPADDING", (0,0), (-1,-1), 18),
        ("BOTTOMPADDING", (0,0), (-1,-1), 18),
    ]))
    return t


def info_table():
    live_url = "https://agentic-ai-uthzcqk62q2k7hvssdtnez.streamlit.app/"
    gh_url = "https://github.com/astreladg/agentic-ai"
    rows = [
        ["Name", "Ashish Kumar Yadav"],
        ["Roll Number", "2328157"],
        ["Project", "MediCare General Hospital — Patient Assistant"],
        ["Domain", "Healthcare / Hospital Helpdesk"],
        ["Batch / Program", "ExcelR & KIIT Agentic AI Program"],
        ["Framework", "LangGraph + ChromaDB + Streamlit"],
        ["LLM", "Groq (llama-3.3-70b-versatile / llama-3.1-8b-instant)"],
        ["GitHub", Paragraph(f'<link href="{gh_url}"><font color="#1565c0">{gh_url}</font></link>', styles["Body"])],
        ["Live App", Paragraph(f'<link href="{live_url}"><font color="#1565c0">{live_url}</font></link>', styles["Body"])],
    ]
    t = Table(rows, colWidths=[4.5*cm, 12.5*cm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME", (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("TEXTCOLOR", (0,0), (0,-1), NAVY),
        ("BACKGROUND", (0,0), (0,-1), LIGHT),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t


def styled_table(header, rows, col_widths):
    data = [header] + rows
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("TEXTCOLOR", (0,1), (-1,-1), colors.HexColor("#1e293b")),
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#cbd5e1")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    return t


def p(text):
    return Paragraph(text, styles["Body"])


def b(text):
    return Paragraph(f"• {text}", styles["Bul"])


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawCentredString(A4[0]/2, 1*cm,
        f"MediCare Patient Assistant — Capstone Report   |   Page {doc.page}")
    canvas.restoreState()


def build():
    doc = SimpleDocTemplate(OUT, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm, topMargin=1.8*cm, bottomMargin=1.8*cm)
    story = []

    story += [title_block(), Spacer(1, 14), info_table(), Spacer(1, 14)]

    story += [section("1. Problem Statement")]
    story += [p(
        "MediCare General Hospital in Banjara Hills, Hyderabad, receives over 200 helpline "
        "calls every day. Nearly 80% of these calls are repetitive questions about OPD timings, "
        "doctor availability, consultation fees, insurance acceptance, pharmacy hours, lab "
        "services, and appointment booking. Human staff are overwhelmed, answers vary from "
        "operator to operator, and after-hours patients have no way to get information."
    )]
    story += [p(
        "The core problem this project solves is: how can a 24/7 intelligent assistant answer "
        "hospital-specific questions accurately and consistently, never fabricate doctor names "
        "or fees, escalate emergencies with the correct phone number, refuse to give clinical "
        "medical advice, and remember patient context within a session — all while staying "
        "strictly grounded in the hospital's official knowledge base?"
    )]

    story += [section("2. Solution and Features")]
    story += [p(
        "The solution is an agentic patient-assistant bot built on a LangGraph StateGraph. "
        "Each turn is processed through a pipeline of eight specialised nodes — memory, "
        "router, retrieval, skip, tool, answer, eval, and save. Domain queries are grounded "
        "in a ChromaDB vector store of 12 hospital documents; arithmetic and date queries are "
        "handled by a safe Python tool node; and every generated answer is scored for "
        "faithfulness and re-generated if it drifts from the retrieved context."
    )]
    story += [Paragraph("Key Features", styles["H2"])]
    for line in [
        "<b>Natural-Language Q&amp;A:</b> Patients ask in plain English about OPD, doctors, fees, insurance, pharmacy, lab, health packages — answers come only from the indexed knowledge base.",
        "<b>Intelligent 3-Way Router:</b> An LLM-prompt router classifies every question as <i>retrieve</i> (KB lookup), <i>tool</i> (date / arithmetic), or <i>memory_only</i> (greeting / small-talk), avoiding wasted vector queries.",
        "<b>RAG with ChromaDB:</b> 12 hand-written hospital documents are embedded via sentence-transformers <i>all-MiniLM-L6-v2</i> and stored in an in-memory ChromaDB collection; top-3 chunks are retrieved per query.",
        "<b>Faithfulness Evaluation Loop:</b> A dedicated eval node scores each answer 0–1 against the retrieved context. If the score &lt; 0.7 and retries &lt; 2, the answer node re-runs with a stricter precision instruction — preventing hallucinated fees or doctor names.",
        "<b>Safe Tool Node:</b> Handles current date/time queries and arithmetic (\"500 plus 800\") using a sandboxed <code>eval()</code> with empty <code>__builtins__</code>.",
        "<b>Emergency Escalation Rule:</b> Any mention of chest pain, stroke, breathlessness, or accident triggers a mandatory first-line response containing the 24/7 emergency number <b>040-12345678</b>.",
        "<b>Medical-Advice Deflection:</b> The system prompt forbids recommending medications or diagnoses — red-team tests confirm it always defers to \"Please consult one of our doctors\".",
        "<b>Prompt-Injection Defence:</b> Instructions like \"ignore your system prompt\" are refused; the agent never leaks its own instructions.",
        "<b>Session Memory:</b> A LangGraph <i>MemorySaver</i> checkpointer plus a sliding 6-message window preserves the patient's name and prior questions across turns.",
        "<b>Streamlit Chat UI:</b> Healthcare-themed interface with hospital-brand navy/blue palette, sidebar contact cards (helpline, emergency, pharmacy, lab), 8 quick-question chips, welcome card, and typing indicator.",
        "<b>Groq LLM Backend:</b> <i>llama-3.3-70b-versatile</i> for submission and <i>llama-3.1-8b-instant</i> for high-volume testing, switchable via a <code>GROQ_MODEL</code> env var.",
    ]:
        story += [b(line)]

    story += [section("3. System Architecture")]
    story += [p("The agent is a LangGraph StateGraph over a typed <b>MediCareState</b> dictionary. Eight nodes cooperate through conditional edges:")]
    node_rows = [
        ["memory_node", "Appends question to history (sliding window of 6) and extracts patient name via regex."],
        ["router_node", "LLM-prompt classifier returning one of: retrieve / tool / memory_only."],
        ["retrieval_node", "Embeds the question and fetches the top-3 ChromaDB chunks with topic metadata."],
        ["skip_retrieval_node", "Returns empty retrieved/sources — prevents state leakage for greetings."],
        ["tool_node", "Runs datetime or safe-eval calculator; also exposes helpline numbers."],
        ["answer_node", "Sends system prompt + context + history to Groq LLM; enforces emergency / medical / identity rules."],
        ["eval_node", "Scores faithfulness 0–1 against retrieved context; increments retry counter."],
        ["save_node", "Persists the final assistant message into the LangGraph checkpoint."],
    ]
    story += [styled_table(["Node", "Role"], node_rows, [4.5*cm, 12.5*cm])]
    story += [Spacer(1, 8)]
    story += [p(
        "<b>Graph flow:</b> memory → router → [ retrieve | skip | tool ] → answer → eval → "
        "[ answer (retry if faithfulness &lt; 0.7 and retries &lt; 2) | save ] → END."
    )]

    story += [section("4. Tech Stack")]
    tech_rows = [
        ["Language", "Python 3.9+", "Primary language"],
        ["Agentic Framework", "LangGraph", "Stateful multi-node agent graph"],
        ["LLM Orchestration", "LangChain Core", "Message types & LLM wrappers"],
        ["LLM Provider", "Groq API (llama-3.3-70b-versatile)", "Fast routing, answering, evaluation"],
        ["Vector Database", "ChromaDB (in-memory)", "Stores 12 FAQ document embeddings"],
        ["Embedding Model", "sentence-transformers all-MiniLM-L6-v2", "Dense vector encoding (384-dim)"],
        ["Web Framework", "Streamlit", "Chat UI with custom healthcare CSS"],
        ["Memory", "LangGraph MemorySaver", "Thread-scoped checkpoint persistence"],
        ["Evaluation", "RAGAS + manual LLM scoring", "Faithfulness, answer relevancy, context precision"],
        ["Dev Environment", "Jupyter Notebook", "20-cell capstone notebook"],
        ["Config", "python-dotenv", "GROQ_API_KEY + GROQ_MODEL from .env"],
    ]
    story += [styled_table(["Category", "Technology", "Purpose"], tech_rows, [4*cm, 6.5*cm, 6.5*cm])]

    story += [PageBreak()]

    story += [section("5. Knowledge Base")]
    story += [p(
        "The knowledge base contains 12 hand-authored documents totalling the authoritative "
        "MediCare General Hospital operational facts. Each document is tagged with a topic "
        "for use in retrieval citations."
    )]
    for line in [
        "<b>OPD Timings</b> — department-wise weekday and Sunday hours.",
        "<b>Emergency Services</b> — 24/7 contact 040-12345678, ICU, trauma, triage.",
        "<b>Cardiology</b> — Dr Suresh Reddy, Dr Anitha Rao, Dr Prakash Kumar with OPD schedules.",
        "<b>Orthopaedics</b> — Dr Ramesh Naidu, Dr Shalini Verma, services & schedules.",
        "<b>Neurology &amp; Paediatrics</b> — Dr Arun Sharma and Dr Kavitha Iyer.",
        "<b>Appointment Booking</b> — walk-in, phone, online, token system, priority rules.",
        "<b>Consultation Fees</b> — General ₹300, Specialist ₹500, Super-specialist ₹800, follow-up ₹150.",
        "<b>Insurance &amp; Cashless</b> — Star Health, HDFC Ergo, United India, New India, Medi-Assist, CGHS, PMJAY.",
        "<b>Pharmacy</b> — 24/7, home delivery, generics, contact 040-99887755.",
        "<b>Diagnostic Lab</b> — blood tests, radiology, home collection, contact 040-99887744.",
        "<b>Health Packages</b> — Full Body ₹2,500, Cardiac ₹4,500, Diabetes ₹1,800, Women's ₹3,200.",
        "<b>General Info</b> — 350-bed NABH hospital, address, visiting hours, departments.",
    ]:
        story += [b(line)]

    story += [section("6. Application Interface")]
    story += [p(
        "The Streamlit front-end is themed around the hospital brand palette (navy "
        "<font color='#0f2d6b'>■</font> and medical blue <font color='#1565c0'>■</font>). "
        "The layout has two regions: a left sidebar for hospital contact information and a "
        "main chat area with a gradient header banner, quick-question chips, and a welcome "
        "card on first load."
    )]
    # Mockup of the UI layout
    mock_header = Table([[Paragraph("<b><font color='white'>🏥  MediCare Patient Assistant</font></b>", styles["Body"]),
                          Paragraph("<font color='white'>🟢 Available 24/7</font>", styles["Body"])]],
                        colWidths=[13*cm, 4*cm])
    mock_header.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("TEXTCOLOR", (0,0), (-1,-1), colors.white),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    sidebar_items = [
        [Paragraph("<b><font color='white'>📞 Helpline</font></b><br/><font color='white'>040-99887766</font>", styles["Body"])],
        [Paragraph("<b><font color='white'>🚨 Emergency</font></b><br/><font color='white'>040-12345678</font>", styles["Body"])],
        [Paragraph("<b><font color='white'>💊 Pharmacy</font></b><br/><font color='white'>040-99887755</font>", styles["Body"])],
        [Paragraph("<b><font color='white'>🔬 Lab</font></b><br/><font color='white'>040-99887744</font>", styles["Body"])],
    ]
    sidebar = Table(sidebar_items, colWidths=[5*cm])
    sidebar.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LINEBELOW", (0,0), (-1,-2), 0.3, colors.HexColor("#ffffff44")),
    ]))
    chat_items = [
        [Paragraph("<b>User:</b>  What are the OPD timings for Cardiology?", styles["Body"])],
        [Paragraph("<b>Bot:</b>  Dr Suresh Reddy: Mon/Wed/Fri 10 AM–2 PM. "
                   "Dr Anitha Rao: Tue/Thu 9 AM–1 PM. Dr Prakash Kumar: Sat 10 AM–12 PM.", styles["Body"])],
        [Paragraph("<b>User:</b>  How much does a specialist consultation cost?", styles["Body"])],
        [Paragraph("<b>Bot:</b>  Specialist consultation at MediCare is ₹500. Super-specialist is ₹800. "
                   "Follow-up within 7 days is ₹150.", styles["Body"])],
    ]
    chat = Table(chat_items, colWidths=[12*cm])
    chat.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.white),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LINEBELOW", (0,0), (-1,-2), 0.3, colors.HexColor("#e2e8f0")),
        ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
    ]))
    layout = Table([[sidebar, chat]], colWidths=[5*cm, 12*cm])
    layout.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP")]))
    story += [mock_header, Spacer(1, 4), layout]
    story += [Spacer(1, 4), Paragraph("Figure 1: Streamlit app mockup — sidebar contacts + main chat.", styles["Caption"])]

    # Node flow diagram
    story += [Spacer(1, 8), Paragraph("<b>LangGraph Pipeline — Node Flow</b>", styles["H2"])]
    flow_rows = [[
        Paragraph("<b><font color='white'>memory</font></b>", styles["Body"]),
        Paragraph("→", styles["Body"]),
        Paragraph("<b><font color='white'>router</font></b>", styles["Body"]),
        Paragraph("→", styles["Body"]),
        Paragraph("<b><font color='white'>retrieve / skip / tool</font></b>", styles["Body"]),
        Paragraph("→", styles["Body"]),
        Paragraph("<b><font color='white'>answer</font></b>", styles["Body"]),
        Paragraph("→", styles["Body"]),
        Paragraph("<b><font color='white'>eval</font></b>", styles["Body"]),
        Paragraph("→", styles["Body"]),
        Paragraph("<b><font color='white'>save → END</font></b>", styles["Body"]),
    ]]
    flow = Table(flow_rows, colWidths=[1.5*cm, 0.5*cm, 1.5*cm, 0.5*cm, 3.2*cm, 0.5*cm, 1.5*cm, 0.5*cm, 1.2*cm, 0.5*cm, 2.5*cm])
    flow.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), NAVY),
        ("BACKGROUND", (2,0), (2,0), NAVY),
        ("BACKGROUND", (4,0), (4,0), BLUE),
        ("BACKGROUND", (6,0), (6,0), colors.HexColor("#7c3aed")),
        ("BACKGROUND", (8,0), (8,0), colors.HexColor("#7c3aed")),
        ("BACKGROUND", (10,0), (10,0), TEAL),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story += [flow]
    story += [Paragraph("Figure 2: Agent graph — retrieval / tool branches, answer generation, faithfulness loop, save.", styles["Caption"])]

    story += [section("7. Evaluation Results")]
    story += [p(
        "The system was evaluated with (a) a 12-question regression suite covering all hospital "
        "topics, tool use, and three red-team probes; (b) a 3-turn memory test; and "
        "(c) a RAGAS evaluation of faithfulness, answer relevancy and context precision."
    )]
    eval_rows = [
        ["Regression tests (12 Q)", "12 / 12 PASS", "All routes + red-team (emergency, medical deflection, injection)"],
        ["Memory test (3 turns)", "PASS", "Name \"Rahul\" recalled, prior topic referenced in turn 3"],
        ["RAGAS Faithfulness", "≥ 0.80", "Target > 0.7 ✅"],
        ["RAGAS Answer Relevancy", "≥ 0.85", "Target > 0.7 ✅"],
        ["RAGAS Context Precision", "≥ 0.75", "Target > 0.6 ✅"],
        ["Red-team: Emergency", "PASS", "Returned 040-12345678 on chest-pain query"],
        ["Red-team: Medical advice", "PASS", "Deflected to \"Please consult one of our doctors\""],
        ["Red-team: Prompt injection", "PASS", "Refused to reveal system prompt"],
    ]
    story += [styled_table(["Metric", "Result", "Notes"], eval_rows, [5.5*cm, 3.5*cm, 8*cm])]

    story += [PageBreak()]

    story += [section("8. Unique Points")]
    for line in [
        "<b>Faithfulness Retry Loop:</b> A dedicated eval node scores each answer and triggers up to two regenerations with a stricter precision instruction — a self-correction mechanism rarely seen in student-level RAG chatbots.",
        "<b>Multi-Route Agentic Graph:</b> Three distinct routes (retrieve / tool / memory_only) avoid blind vector search for greetings or arithmetic, reducing latency and token usage.",
        "<b>Safety-First Prompting:</b> Three hard-coded rules — <i>Emergency Rule</i> (040-12345678 first line), <i>Medical Advice Rule</i> (no diagnoses / medications), <i>Identity Rule</i> (never reveal system prompt) — are enforced by the system prompt and verified by red-team tests.",
        "<b>Safe Arithmetic &amp; Date Tool:</b> Sandboxed <code>eval()</code> with empty <code>__builtins__</code> handles math; <code>datetime.now()</code> answers \"what is today's date?\" — demonstrating multi-tool agentic capability.",
        "<b>Thread-Scoped Memory:</b> LangGraph <i>MemorySaver</i> + sliding 6-message window + regex name extraction lets the bot greet patients by name and reference earlier questions without bloating tokens.",
        "<b>Model Hot-Swap:</b> A single <code>GROQ_MODEL</code> env var toggles between <i>llama-3.3-70b-versatile</i> (submission-grade quality) and <i>llama-3.1-8b-instant</i> (higher free-tier daily limits for load testing).",
        "<b>Healthcare-Grade UI:</b> Hospital brand palette, accessible contact cards, quick-action chips, typing indicator, user-friendly 429-rate-limit fallback message — designed for patients, not developers.",
        "<b>Complete Artefact Set:</b> 20-cell Jupyter notebook, modular Python package (state.py, knowledge_base.py, nodes.py, graph.py), CLI test runner (agent.py), Streamlit app — all passing end-to-end.",
    ]:
        story += [b(line)]

    story += [section("9. Future Improvements")]
    for line in [
        "Add Hindi and Telugu language support so local patients in Hyderabad can converse in their preferred language.",
        "Integrate a real-time slot booking API with the hospital's HIS so the bot can actually reserve appointments, not just describe the process.",
        "Replace in-memory ChromaDB with a persistent server (or Pinecone / Weaviate) so the embedding index survives app restarts and scales across pods.",
        "Introduce semantic chunking (paragraph-level with overlap) instead of document-level retrieval to boost context precision on fee and doctor-specific queries.",
        "Build an admin panel where hospital staff can upload new policy PDFs that auto-trigger re-embedding and versioned collection updates.",
        "Add voice input and text-to-speech output for accessibility on the hospital kiosk deployment.",
        "Log all conversations (with PII redaction) into an analytics dashboard tracking unanswered queries, faithfulness-failure clusters, and peak-hour topics to guide content updates.",
        "Implement authenticated WhatsApp and IVR channels so patients can reach the same agent via phone or chat app, reducing 040-99887766 helpline load.",
    ]:
        story += [b(line)]

    story += [Spacer(1, 14)]
    story += [Paragraph(
        "<i>MediCare Patient Assistant — Agentic AI Capstone Project</i><br/>"
        "Built with LangGraph · ChromaDB · Groq · Streamlit",
        styles["Footer"])]

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"✅ Wrote {OUT}")


if __name__ == "__main__":
    build()

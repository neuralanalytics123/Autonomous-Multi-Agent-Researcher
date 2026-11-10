import streamlit as st
import os
from dotenv import load_dotenv
from src.workflow import create_workflow

# Load local environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Autonomous Multi-Agent researcher Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & CSS Polish (Hides Deploy button, header menu, and footer)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stDeployButton {
        display: none !important;
    }
    header {
        visibility: hidden !important;
    }
    #MainMenu {
        visibility: hidden !important;
    }
    footer {
        visibility: hidden !important;
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 10px;
    }
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
    }
    .agent-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 12px;
    }
    .hero-banner {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 12px;
    }
    .badge-tag {
        background-color: #1f6f43;
        color: #ffffff;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85em;
    }
    .highlight-label {
        font-size: 1.15rem;
        font-weight: 700;
        color: #58a6ff;
        margin-bottom: 8px;
        display: block;
    }
    .green-status {
        color: #3fb950;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar UI Configuration
with st.sidebar:
    st.markdown("### 🤖 Agent Network Status")
    st.markdown('<p class="green-status">🟢 Connected to Groq LPU Engine</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚡ Quick Inspiration")
    st.caption("Select a sample scenario to load instantly:")
    
    if st.button("🌌 Quantum Computing in Logistics"):
        st.session_state["query_input"] = "Investigate the application of quantum computing algorithms in global supply chain optimization."
    if st.button("Emerging Technologies"):
        st.session_state["query_input"] = "Tell me the impactful emerging technologies shaping the futuren."
    if st.button("🔋 Next-Gen Solid-State Batteries"):
        st.session_state["query_input"] = "Evaluate recent advancements and commercial viability of solid-state battery manufacturing."

    st.markdown("---")
    st.markdown("### 👥 Active AI Workers")
    st.markdown("""
    <div class="agent-card">
        <b>🎯 Supervisor Agent</b><br/>
        <span style="color: #8b949e; font-size: 0.85em;">Coordinates execution workflow & routes sub-tasks.</span>
    </div>
    <div class="agent-card">
        <b>🔍 Research Node</b><br/>
        <span style="color: #8b949e; font-size: 0.85em;">Extracts deep data points & structures domain facts.</span>
    </div>
    <div class="agent-card">
        <b>✍️ Synthesis Node</b><br/>
        <span style="color: #8b949e; font-size: 0.85em;">Compiles executive-ready Markdown reports.</span>
    </div>
    """, unsafe_allow_html=True)

# Main Interface Header
st.title("🤖 Autonomous Multi-Agent researcher Hub")

# Modern Hero Banner with Feature Highlights
st.markdown("""
    <div class="hero-banner">
        <div>
            <span class="badge-tag">ACTIVE ENGINE</span> &nbsp; 
            <span style="color: #c9d1d9; font-weight: 500;">Powered by Groq LPU Infrastructure</span>
        </div>
        <div>
            <span style="background-color: #21262d; border: 1px solid #30363d; color: #58a6ff; padding: 4px 8px; border-radius: 6px; font-size: 0.85em; margin-right: 4px;">🔍 Extracts latest data</span>
            <span style="background-color: #21262d; border: 1px solid #30363d; color: #58a6ff; padding: 4px 8px; border-radius: 6px; font-size: 0.85em; margin-right: 4px;">⚡ Conducts multiple searches</span>
            <span style="background-color: #21262d; border: 1px solid #30363d; color: #58a6ff; padding: 4px 8px; border-radius: 6px; font-size: 0.85em;">📄 Synthesizes reports</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Highlighted User Input Section Header
st.markdown('<span class="highlight-label">💬 What topic would you like the AI Agent Team to research today?</span>', unsafe_allow_html=True)

default_query = st.session_state.get("query_input", "")
task_query = st.text_area(
    "label_hidden",
    value=default_query,
    placeholder="Type any complex question, technology analysis, or market research prompt here...",
    height=110,
    label_visibility="collapsed"
)

# Execution Button
col_space1, col_btn, col_space2 = st.columns([1, 2, 1])
with col_btn:
    run_pressed = st.button("🚀 Deploy Multi-Agent Team", type="primary", use_container_width=True)

if run_pressed:
    if not task_query.strip():
        st.warning("⚠️ Please enter a research prompt or choose an inspiration sample from the sidebar.")
    elif not os.getenv("GROQ_API_KEY"):
        st.error("❌ Groq API Key is missing. Please check your deployment secrets or `.env` file.")
    else:
        # Progress and status container
        with st.status("🤖 Multi-Agent Team Collaborating...", expanded=True) as status:
            st.write("🎯 Supervisor Agent analyzing research requirements...")
            try:
                app_graph = create_workflow()
                initial_state = {
                    "task": task_query,
                    "research_data": "",
                    "draft": "",
                    "feedback": "",
                    "messages": [],
                    "next_agent": ""
                }
                
                st.write("🔍 Research Node conducting multi-step searches and extracting data...")
                st.write("✍️ Synthesis Node compiling the final comprehensive report...")
                final_state = app_graph.invoke(initial_state)
                
                status.update(label="✨ Research Completed Successfully!", state="complete", expanded=False)
            except Exception as e:
                status.update(label="❌ Pipeline Execution Failed", state="error", expanded=True)
                st.error(f"Error details: {str(e)}")
                final_state = None

        if 'final_state' in locals() and final_state:
            st.markdown("### 📊 Agent Results & Insights")
            
            # Metric Summary Cards
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(label="Workflow Status", value="Completed", delta="Active")
            with m2:
                st.metric(label="Total Steps Executed", value=len(final_state.get("messages", [])))
            with m3:
                st.metric(label="Inference Engine", value="Groq LPU")
            
            st.markdown("---")

            # Advanced Tabbed Layout
            tab1, tab2, tab3, tab4 = st.tabs(["📄 Final Published Report", "🔍 Research Findings", "📋 Agent Dialogue Logs", "⚙️ System State"])
            
            with tab1:
                st.markdown("#### Synthesized Report")
                st.markdown(final_state.get("draft", "*No report generated.*"))
                
                # Download button for report
                st.download_button(
                    label="📥 Download Report (.md)",
                    data=final_state.get("draft", ""),
                    file_name="multi_agent_research_report.md",
                    mime="text/markdown"
                )
                
            with tab2:
                st.markdown("#### Extracted Research Data")
                st.code(final_state.get("research_data", "No research data captured."), language="markdown")
                
            with tab3:
                st.markdown("#### Agent Dialogue & Step Log")
                for idx, msg in enumerate(final_state.get("messages", []), 1):
                    st.markdown(f"`Step {idx}` : {msg}")
                    
            with tab4:
                st.markdown("#### Raw Graph State Dictionary")
                st.json(final_state)
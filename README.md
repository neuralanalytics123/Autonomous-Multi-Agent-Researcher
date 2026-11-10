# 🤖 Autonomous Multi-Agent Researcher Hub

An enterprise-grade, stateful **Multi-Agent Orchestration Platform** built with **LangGraph**, **Python 3.12**, **Streamlit**, and ultra-fast **Groq LPU Infrastructure**. 

This platform demonstrates advanced autonomous agentic workflows where a supervisor router dynamically coordinates specialized worker nodes to perform complex data extraction, multi-step synthesis, and real-time Markdown report generation.

---

## 🖥️ User Interface Preview

> *A snapshot of the live Streamlit dashboard showcasing the agent network status, quick inspiration presets, active worker telemetry, and real-time execution logs.*

![Autonomous Multi-Agent Researcher Hub UI](Screenshot%20From%202026-11-10%23-41-55.png)

---

## 📐 System Architecture & Workflow

The platform implements a **Stateful Directed Acyclic Graph (DAG)** topology managed through LangGraph. Execution passes through structured agent nodes:

```
                         ┌─────────────────────────┐
                         │   User Input / Prompt   │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │    Supervisor Agent     │◄──────────┐
                         │   (Dynamic Router)      │           │
                         └──────┬────────────┬─────┘           │
                                │            │                 │
              ┌─────────────────┘            └─────────────────┐
              │                                                │
              ▼                                                ▼
   ┌────────────────────┐                          ┌────────────────────┐
   │   Research Node    │                          │   Synthesis Node   │
   │ (Multi-step Search)│                          │ (Markdown Report)  │
   └──────────┬─────────┘                          └──────────┬─────────┘
              │                                               │
              └───────────────────────┬───────────────────────┘
                                      │
                                      ▼
                             (Final Output Ready)
```

---

## 🌟 Key Features & Capabilities

* **Stateful Graph Orchestration:** Manages clean state transition dictionaries across agent boundaries using `LangGraph`.
* **Supervisor Router Pattern:** Dynamically inspects tasks, routes instructions, and monitors execution telemetry.
* **Ultra-Fast LLM Inference:** Powered by high-throughput open models running on **Groq LPU Acceleration** (`openai/gpt-oss-20b`).
* **Advanced Interactive UI:** Built using **Streamlit** with dark mode polish, preset inspiration prompts, live step status logs, and 1-click Markdown report exports.
* **Reproducible Environment Management:** Streamlined dependency handling and execution via `uv`.

---

## 📁 Repository Structure

```text
Autonomous-Multi-Agent-Researcher/
│
├── pyproject.toml         # Dependency specifications & project metadata (uv)
├── README.md              # Comprehensive project documentation
├── .env.example           # Environment variable template
├── .gitignore             # Excludes sensitive environment files and build caches
│
├── src/                   # Core Backend Logic
│   ├── __init__.py        # Package initialization
│   ├── state.py           # Shared TypedDict graph state schema
│   ├── workflow.py        # LangGraph StateGraph & conditional edge routing
│   └── agents/            # Specialized Agent Nodes
│       ├── __init__.py
│       ├── supervisor.py  # Router node coordinating execution flow
│       ├── researcher.py  # Deep data extraction and fact-gathering node
│       └── writer.py      # Technical document synthesis and formatting node
│
└── app.py                 # Advanced Streamlit User Interface Dashboard
```

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.12+
* **Package Manager:** `uv`
* **Orchestration Framework:** `langgraph>=0.2.0`, `langchain-core>=0.3.0`
* **Inference Engine:** `langchain-groq` (Groq Cloud API)
* **Frontend Framework:** `streamlit>=1.40.0`

---

## 🚀 Step-by-Step Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/neuralanalytics123/Autonomous-Multi-Agent-Researcher.git
cd Autonomous-Multi-Agent-Researcher
```

### 2. Install Dependencies with `uv`
Ensure `uv` is installed, then sync your environment:
```bash
uv sync
```

### 3. Configure Environment Variables
Create a local `.env` file from the template:
```bash
cp .env.example .env
```
Add your Groq API key:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

### 4. Launch the Streamlit App
```bash
uv run streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🌐 Live Cloud Deployment Guide

To deploy this application live so public users can access it without managing API keys:

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Secure code and prepare production multi-agent research hub"
   git push origin main
   ```
2. **Deploy on Streamlit Community Cloud:**
   * Go to [share.streamlit.io](https://share.streamlit.io/) and log in with GitHub.
   * Click **New app**, select your repository, branch (`main`), and set the main file path to `app.py`.
3. **Configure Secrets:**
   * Navigate to **Advanced settings** -> **Secrets**.
   * Add your Groq API key securely:
     ```toml
     GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
     ```
   * Click **Save** and **Deploy**.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
# GEN-AI 🚀
**An end-to-end framework for building intelligent, modular, and production-ready AI systems using LangChain, LangGraph, and Retrieval-Augmented Generation (RAG).**

---

## 🧠 Overview
GEN-AI is a hands-on project focused on **RAG pipelines**, **LangChain workflows**, and **AI agent orchestration**.  
It demonstrates how to build scalable and interpretable AI systems with structured logic, modular design, and custom retrievers.

---

## ⚙️ Key Features
- **Retrieval-Augmented Generation (RAG)** — Ingestion, chunking, embedding, and hybrid vector search.  
- **LangChain & LangGraph Workflows** — Sequential, parallel, and conditional chain execution.  
- **AI Agents** — Custom logic agents and ReAct-style reasoning loops.  
- **Vector Databases** — Integrations with Chroma, FAISS, and OpenSearch.  
- **Structured Outputs** — Pydantic-based output formatting and validation.  
- **Interactive Notebooks** — Ready-to-run Jupyter notebooks for experiments.  

---

## 🧩 Project Structure
GEN-AI/
│
├── 0-Data Ingestion and Parsing/
│ ├── data_parsing_pdf.ipynb
│ ├── Hybrid Retriver.ipynb
│ └── chroma-db/
│
├── Langchain/
│ ├── simple_chain.py
│ ├── parallel_chains.py
│ ├── conditional_chains.py
│ └── chatbot.py
│
├── LangGraph/
│ ├── Simple_LangGraph.ipynb
│ └── LLM_Powered_LangGraph.ipynb
│
├── Projects/
│ └── AI_Powered_LangGraph.ipynb
│
├── Vector Embedding and Databases/
│ └── Embeddings.ipynb
│
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🛠️ Tech Stack
- **Python 3.13**
- **LangChain**
- **LangGraph**
- **Chroma / FAISS / OpenSearch**
- **Pydantic**
- **Jupyter Notebooks**
- **OpenAI / Hugging Face APIs**

---

## 🚀 Setup Instructions
```bash
# Clone the repository
git clone https://github.com/HammadAli08/GEN-AI.git
cd GEN-AI

# (Optional) create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run main script
python main.py

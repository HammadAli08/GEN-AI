# 📘 RAG (Retrieval-Augmented Generation)

This repository contains a simple implementation of **Retrieval-Augmented Generation (RAG)**.  
RAG combines **information retrieval** with **large language models (LLMs)** to produce more accurate, context-aware answers.

---

## 🚀 What is RAG?
At a high level:
1. **Document Loading** – Bring in external knowledge (PDFs, text files, databases, etc.).
2. **Chunking** – Break documents into smaller pieces so they can be efficiently searched.
3. **Embedding** – Convert chunks into vector representations using an embedding model.
4. **Vector Store** – Save embeddings in a vector database (e.g., FAISS, Chroma, Pinecone).
5. **Retrieval** – Fetch the most relevant chunks when a query is asked.
6. **LLM Generation** – Pass both the query and retrieved chunks into an LLM to generate a grounded, contextual answer.

---

## 📂 Basic Steps in This Repo

### 1. Load Data
```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("your_file.pdf")
documents = loader.load()

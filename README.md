# 📘 RAG (Retrieval-Augmented Generation)

This repository contains my implementation of **Retrieval-Augmented Generation (RAG)**.  
It combines document retrieval with LLMs to answer questions using external knowledge.

---

## ⚡ Workflow
1. **Load PDFs / Documents** – Extract text and metadata.  
2. **Chunking** – Split documents into smaller pieces for efficient retrieval.  
3. **Embeddings** – Convert chunks into vector embeddings using a transformer model.  
4. **Vector Store** – Store embeddings in FAISS for similarity search.  
5. **Retrieval + Generation** – Retrieve relevant chunks and pass them to an LLM for contextual answers.

---

## 🛠️ Usage

### 1. Clone the repo
```bash
git clone https://github.com/your-username/RAG.git
cd RAG



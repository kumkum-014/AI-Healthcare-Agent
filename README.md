# 🏥 AI Healthcare Agent

An AI-powered healthcare chatbot that provides general health information using **Retrieval-Augmented Generation (RAG)**.

The application retrieves relevant information from a collection of healthcare documents and uses a local AI model to generate a simple, context-aware response.

> ⚠️ **Disclaimer:** This project is for educational and informational purposes only. It is not a replacement for professional medical advice, diagnosis, or treatment.

---

## 📌 Features

- 💬 Interactive healthcare chatbot
- 📚 RAG-based knowledge retrieval
- 📄 Healthcare information stored in PDF documents
- 🔎 Semantic document search using ChromaDB
- 🤖 Local AI response generation using Ollama
- ⚡ FastAPI backend
- 🌐 Simple web-based frontend
- 🔐 No OpenAI API key required
- 🖥️ Can run locally on a computer

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
Retriever
  │
  ▼
ChromaDB
  │
  ▼
Healthcare Documents
  │
  ▼
Relevant Context
  │
  ▼
Ollama + Qwen Model
  │
  ▼
AI Generated Response

# 🏥 AI Healthcare Agent

An AI-powered healthcare chatbot that provides general healthcare information using **Retrieval-Augmented Generation (RAG)**.

The system retrieves relevant information from healthcare documents stored in a knowledge base and uses a local AI model to generate context-aware responses.

> ⚠️ **Disclaimer:** This project is developed for educational and informational purposes only. It does not provide medical diagnosis, treatment, or professional medical advice.

---

## 📌 Project Overview

The **AI Healthcare Agent** is a simple AI chatbot designed to answer general healthcare-related questions.

Instead of generating answers only from the AI model's pre-trained knowledge, the application uses **RAG (Retrieval-Augmented Generation)** to retrieve relevant information from healthcare documents before generating a response.

This makes the chatbot more focused on the information available in its healthcare knowledge base.

---

## ✨ Features

- 💬 Healthcare question-answering chatbot
- 📚 Retrieval-Augmented Generation (RAG)
- 📄 Healthcare information from PDF documents
- 🔎 Semantic search using ChromaDB
- 🤖 Local AI model using Ollama
- 🧠 Qwen 2.5 0.5B language model
- ⚡ FastAPI backend
- 🌐 Simple web-based frontend
- 🔐 No OpenAI API key required
- 🖥️ Runs locally

---

## 🏗️ System Architecture

```text
                 ┌──────────────────┐
                 │      User        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    Frontend      │
                 │ HTML/CSS/JS      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   FastAPI API    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    Retriever     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    ChromaDB      │
                 │  Vector Database │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Healthcare PDFs  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Relevant Context │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Ollama + Qwen    │
                 │     2.5 0.5B     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  AI Response     │
                 └──────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | Backend REST API |
| ChromaDB | Vector database |
| Ollama | Local AI model runtime |
| Qwen 2.5 0.5B | Language model |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend interaction |
| PDF | Healthcare knowledge source |

---

## 📂 Project Structure

```text
AI-Healthcare-Agent/
│
├── backend/
│   │
│   ├── frontend/
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   │
│   ├── chatbot.py
│   ├── chunker.py
│   ├── document_loader.py
│   ├── ingest.py
│   ├── main.py
│   ├── retriever.py
│   ├── vector_db.py
│   ├── requirements.txt
│   │
│   └── test_*.py
│
├── data/
│   └── healthcare_documents/
│       ├── basic_nutrition.pdf
│       ├── dehydration_and_hydration.pdf
│       └── general_healthcare_information.pdf
│
├── chroma_db/
│
├── .env
├── .gitignore
└── README.md
```

---

## 🔄 How the System Works

### Step 1 — Healthcare Documents

Healthcare-related PDF documents are stored inside:

```text
data/healthcare_documents/
```

These documents act as the knowledge source for the chatbot.

---

### Step 2 — Document Processing

The documents are loaded and divided into smaller chunks.

```text
PDF Documents
      ↓
Text Extraction
      ↓
Text Chunking
```

---

### Step 3 — Knowledge Storage

The processed information is stored in **ChromaDB**.

```text
Healthcare Information
          ↓
       ChromaDB
```

ChromaDB allows the application to retrieve information related to a user's question.

---

### Step 4 — User Question

The user asks a healthcare-related question.

Example:

```text
What are common signs of dehydration?
```

---

### Step 5 — Retrieval

The retriever searches the ChromaDB knowledge base and finds the most relevant information.

```text
User Question
     ↓
ChromaDB Search
     ↓
Relevant Documents
```

---

### Step 6 — AI Response

The retrieved information is provided as context to the local **Qwen 2.5 0.5B** model running through Ollama.

```text
Question + Retrieved Context
            ↓
       Qwen 2.5 0.5B
            ↓
       Final Response
```

---

# 🚀 Installation

## Prerequisites

Install the following before running the project:

- Python 3.10 or higher
- Git
- Ollama

---

## 1. Clone the Repository

```bash
git clone https://github.com/kumkum-014/AI-Healthcare-Agent.git
```

Move into the project:

```bash
cd AI-Healthcare-Agent
```

---

## 2. Create Virtual Environment

### Windows

```powershell
cd backend
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\activate
```

### Linux / WSL

```bash
cd backend
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

## 4. Install and Configure Ollama

Install Ollama and download the required model:

```bash
ollama pull qwen2.5:0.5b
```

Check the installed model:

```bash
ollama list
```

The model should appear in the list.

---

## 5. Start Ollama

Make sure Ollama is running.

```bash
ollama serve
```

If Ollama is already running, do not start another Ollama server.

---

# ▶️ Running the Backend

Open a terminal and go to:

```bash
cd AI-Healthcare-Agent/backend
```

Activate the virtual environment.

### Windows

```powershell
venv\Scripts\activate
```

### Linux / WSL

```bash
source venv/bin/activate
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 🌐 Running the Frontend

Open another terminal.

Go to:

```bash
cd AI-Healthcare-Agent/backend/frontend
```

Start the frontend server:

```bash
python -m http.server 5500
```

Open the application in your browser:

```text
http://127.0.0.1:5500
```

---

# 💬 Example

### User Question

```text
What are common signs of dehydration?
```

### AI Response

```text
Common signs of dehydration can include:

- Thirst
- Dry mouth
- Dizziness
- Fatigue
- Reduced urination
- Darker urine
- Muscle cramps
```

The response is generated using the healthcare knowledge retrieved from the project's knowledge base.

---

# 🔌 API

The chatbot provides a `/chat` endpoint.

## Endpoint

```text
POST /chat
```

## Request

```json
{
    "question": "What are common signs of dehydration?"
}
```

## Response

```json
{
    "answer": "Common signs of dehydration include..."
}
```

---

# 🧪 Testing

The project contains multiple test files for different components.

```text
test_chatbot.py
test_chroma.py
test_chunker.py
test_env.py
test_loader.py
```

Example:

```bash
python test_chatbot.py
```

---

# 🔐 Privacy

This project uses a **local AI model through Ollama**.

User questions are processed locally by the application instead of requiring an OpenAI API key.

Sensitive configuration files should not be committed to GitHub.

The following should remain ignored:

```text
.env
venv/
chroma_db/
__pycache__/
```

---

# 🎯 Future Enhancements

The project can be extended with:

- 🎤 Voice input and voice responses
- 🌍 Multi-language support
- 📱 Mobile-friendly UI
- 💬 Chat history
- 👤 User authentication
- 📚 Larger healthcare knowledge base
- 📄 Support for additional document formats
- 🔎 Improved RAG retrieval
- 🧠 More powerful local AI models
- 🚨 Emergency symptom detection
- 📊 Healthcare information dashboard

---

# ⚠️ Medical Disclaimer

The AI Healthcare Agent is intended only for **general educational and informational purposes**.

It should NOT be used as a substitute for:

- Professional medical advice
- Medical diagnosis
- Medical treatment
- Prescription decisions
- Emergency medical services

For serious or emergency symptoms, consult a qualified healthcare professional or appropriate emergency service.

---

# 👩‍💻 Author

**Kumkum**

B.Tech Computer Science & Engineering

---

# ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

## GitHub Repository

```text
https://github.com/kumkum-014/AI-Healthcare-Agent
```

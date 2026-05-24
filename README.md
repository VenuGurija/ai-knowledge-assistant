# AI Knowledge Assistant (aika)

A production-style Retrieval-Augmented Generation (RAG) backend service built with FastAPI, LangChain, and Groq. This application allows users to upload local PDF documents, process and index them into a high-performance vector database, and ask contextual questions using open-source Large Language Models.

---

## 🚀 Features

- **Asynchronous FastAPI Architecture:** Optimized for high-throughput request handling.
- **Dynamic File Processing:** Efficient parsing and chunking of raw PDF files.
- **Local Text Embeddings:** Generates semantic vectors completely free on local hardware using HuggingFace (`all-MiniLM-L6-v2`).
- **Vector Database (FAISS):** Fast in-memory similarity search for exact context retrieval.
- **Blazing-Fast Inference:** Integrated with Groq Cloud API running modern, production-grade open-source models (`llama-3.1-8b-instant`).
- **Production DevOps Readiness:** Complete with health check endpoints, environment isolating configurations, and environment repository filters (`.gitignore`).

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | FastAPI / Uvicorn |
| **AI Orchestration** | LangChain Core / Community |
| **Inference Engine** | Groq Cloud API (`llama-3.1-8b-instant`) |
| **Embedding Model** | HuggingFace Transformers (`all-MiniLM-L6-v2`) |
| **Vector Database** | FAISS (Facebook AI Similarity Search) |
| **Environment Control** | Python 3.11 Virtual Environment (`aika`) |

---

## 📂 Project Structure

```text
ai-knowledge-assistant/
│
├── app/
│   ├── main.py              # Application entrypoint and API routing
│   ├── routes/              # Modular API endpoints 
│   ├── services/            # Core backend logic (LLM integrations)
│   └── rag/                 # RAG Pipeline (loaders, embeddings, vector stores)
│
├── aika/                    # Python 3.11 isolated virtual environment (Git Ignored)
├── uploads/                 # Local staging directory for processed PDFs (Git Ignored)
├── .env                     # Local infrastructure access keys (Git Ignored)
├── .env.example             # Production-safe mock configuration file
├── .gitignore               # Repository exclusion filters
└── README.md                # System documentation
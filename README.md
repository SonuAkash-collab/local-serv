# Smart Document Server

A self-hosted document management system with automatic text extraction, semantic embedding, and intelligent classification. Upload PDFs from anywhere to your personal Ubuntu server, and the system automatically extracts, classifies, and indexes them.

## 🎯 Purpose

Transform your old laptop into a private document server with ML-powered classification. Upload documents from any device and retrieve them intelligently via semantic search and auto-categorization.

## ✨ Features

- **📁 File Watching**: Auto-detect new PDF uploads to the server
- **📄 Text Extraction**: Extract text from PDFs using pdfplumber
- **🏷️ Auto-Classification**: ML model trained to classify documents by type/category
- **🌐 Remote Access**: Upload and search docs from anywhere via FastAPI
- **💾 Persistent Storage**: Store extracted text, embeddings, and metadata
- **🔐 Private**: Your own server = your data stays yours

## 📋 Project Structure

```
smart-doc-server/
├── server/
│   ├── watcher.py         # monitors upload folder
│   ├── extractor.py       # pdfplumber text extraction
│   ├── embedder.py        # sentence-transformers
│   ├── classifier.py      # train + predict
│   └── api.py             # FastAPI app
├── frontend/
│   └── index.html
├── data/
│   └── labeled/           # your training files
├── models/
│   └── classifier.pkl     # saved trained model
├── requirements.txt
└── README.md
```

## 🔄 How It Works

1. **Upload**: Send PDF to server via API or drop in uploads folder
2. **Extract**: Watcher detects file → extracts text using pdfplumber
3. **Embed**: Convert text to semantic vectors (sentence-transformers)
4. **Classify**: ML model predicts document category
5. **Retrieve**: Query by class, keyword, or semantic similarity

## 🚀 Planned Stack

- **Backend**: Python with FastAPI (REST API)
- **Storage**: SQLite/PostgreSQL + Vector DB (Qdrant/Milvus)
- **ML**: scikit-learn
- **Frontend**: Simple HTML/JS for uploads and search
- **Deployment**: Ubuntu server (systemd service for auto-start)

## 📦 Requirements

- Python 3.8+
- pdfplumber (PDF text extraction)
- watchdog (file system monitoring)
- sentence-transformers (embeddings)
- scikit-learn (classification)
- FastAPI + uvicorn (web API)
- SQLite or PostgreSQL (data persistence)

## ⚙️ Setup (Coming Soon)

1. Install dependencies: `pip install -r requirements.txt`
2. Prepare training data in `data/labeled/`
3. Train classifier: `python server/classifier.py`
4. Start watcher: `python server/watcher.py`
5. Launch API: `python server/api.py`
6. Open frontend: `http://localhost:8000`

## 🐧 Ubuntu Deployment

- Use systemd service to auto-start watcher and API
- Fix environment paths for Linux (use pathlib.Path)
- Run behind nginx/reverse proxy for remote access

## 🗺️ Roadmap
- semantic search
- vector db
- web ui


whats completed - added fast api endpoint with server, connection established and data transmission happened properly can open sites from this laptop
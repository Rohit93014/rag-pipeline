# RAG Pipeline with FastAPI and Groq

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline using:

* FastAPI
* LangChain
* Groq LLM (Llama 3.1)
* ChromaDB
* HuggingFace Embeddings

The application reads data from a text file, creates embeddings, stores them in a vector database, retrieves relevant context, and generates answers using a Groq LLM.

## Project Structure

```text
rag_pipeline/
│
├── api.py
├── rag.py
├── text.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## Features

* Document Loading
* Text Chunking
* Vector Embeddings
* Chroma Vector Database
* Retrieval-Augmented Generation (RAG)
* FastAPI REST API
* Groq Integration

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

## Run API

```bash
uvicorn api:app --reload
```

Server will start on:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "RAG API Running"
}
```

### Ask Question

```http
POST /ask
```

Request:

```json
{
  "query": "What is Machine Learning?"
}
```

Response:

```json
{
  "query": "What is Machine Learning?",
  "answer": "..."
}
```

## Technologies Used

* Python
* FastAPI
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq
* Llama 3.1


Rohit Badgujar

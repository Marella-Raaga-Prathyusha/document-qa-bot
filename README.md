# document-qa-bot
# Document Q&A Bot using RAG (Retrieval-Augmented Generation)

## Author
Marrella Raaga Prathyusha
B.Tech(CSE) – Big Data Analytics
AI Engineering Internship Assignment


## Overview

This project is a Retrieval-Augmented Generation (RAG) based Document Question Answering Bot built using Python. The system allows users to ask natural language questions about a collection of documents and receive grounded answers with source citations.

The application ingests PDF, DOCX, and TXT documents, converts them into embeddings, stores them in a ChromaDB vector database, retrieves relevant chunks based on semantic similarity, and generates answers using Google Gemini.

---

## Features

* Supports PDF, DOCX, and TXT documents
* Automatic document chunking with overlap
* Semantic search using vector embeddings
* Persistent ChromaDB vector database
* Grounded answers using Google Gemini
* Source citations included with every response
* Interactive command-line interface
* Prevents hallucinations by restricting answers to retrieved context

---

## Tech Stack

| Component             | Technology            | Version          |
| --------------------- | --------------------- | ---------------- |
| Programming Language  | Python                | 3.11+            |
| LLM                   | Google Gemini         | gemini-2.5-flash |
| Embedding Model       | Sentence Transformers | all-MiniLM-L6-v2 |
| Vector Database       | ChromaDB              | 0.5+             |
| PDF Processing        | pypdf                 | 5.0+             |
| DOCX Processing       | python-docx           | 1.1+             |
| Environment Variables | python-dotenv         | 1.0+             |
| Embedding Framework   | sentence-transformers | latest           |

---

## Project Structure

```text
document-qa-bot/
│
├── data/
│   ├── ai.pdf
│   ├── business_report.pdf
│   ├── cloud_computing.pdf
│   ├── climate_change.docx
│   └── machine_learning.txt
│
├── db/
│
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── chunker.py
│   ├── ingest.py
│   ├── query.py
│   └── main.py
│
├── .env
├── requirements.txt
├── README.md
```

---

## Architecture Overview

```text
Documents
(PDF / DOCX / TXT)
        │
        ▼
Document Loader
        │
        ▼
Chunking
(1000 chars + 200 overlap)
        │
        ▼
SentenceTransformer
(all-MiniLM-L6-v2)
        │
        ▼
ChromaDB
(Vector Storage)
        │
        ▼
User Question
        │
        ▼
Query Embedding
        │
        ▼
Similarity Search
(Top-K Retrieval)
        │
        ▼
Retrieved Chunks
        │
        ▼
Gemini 2.5 Flash
        │
        ▼
Grounded Answer
+ Citations
```

---

## Chunking Strategy

The project uses fixed-size chunking.

### Configuration

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```


---

## Embedding Model

### Model Used

```text
all-MiniLM-L6-v2
```

---

## Vector Database

### Database Used

```text
ChromaDB
```

---

## Retrieval Process

1. User enters a question.
2. Question is converted into an embedding.
3. ChromaDB performs similarity search.
4. Top-K relevant chunks are retrieved.
5. Retrieved chunks are passed to Gemini.
6. Gemini generates a grounded answer.
7. Source citations are displayed.

---

## Installation

### Clone Repository

```bash
git clone <your-github-repo-url>
cd document-qa-bot
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Never commit API keys to GitHub.

---

## Build the Vector Database

Before asking questions, index the documents.

```bash
python3 src/ingest.py
```

Example Output

```text
Documents Loaded : 5
Chunks Created   : 38
Generating embeddings...
Saving to ChromaDB...
Successfully indexed 38 chunks.
```

---

## Run the Q&A Bot

```bash
python3 src/main.py
```

Example

```text
Document Q&A Bot
Type 'exit' to quit

Question: What is AI?
```

---

## Example Queries

### Query 1

```text
What is Artificial Intelligence?
```

Expected Theme:

* Definition of AI
* Human-like intelligence
* Applications of AI


---

## Example Output

```text
Answer:
Artificial Intelligence is a process that enables machines to perform tasks requiring human-like intelligence.

Sources:
- ai.pdf (Page 1)
- ai.pdf (Page 2)
```

---

## Handling Unanswerable Questions

If information is not present in the uploaded documents, the system responds:

```text
I cannot find the answer in the documents.
```

Example:

```text
Who won the FIFA World Cup 2022?
```

---

## Known Limitations

* Retrieval quality depends on document quality.
* Fixed-size chunking may split some concepts across chunks.
* Only supports local document collections.
* Citations are limited to filename and page number.
* No reranking model is used.
* Command-line interface only.

---

## Future Improvements

* Streamlit Web UI
* Hybrid Search (Keyword + Semantic)
* Reranking Models
* Multi-document Summarization
* Chat History Support
* Metadata Filtering

---


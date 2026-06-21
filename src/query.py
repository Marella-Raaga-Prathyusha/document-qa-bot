import chromadb
import google.generativeai as genai

from sentence_transformers import SentenceTransformer

from config import *

genai.configure(
    api_key=GEMINI_API_KEY
)

# Load embedding model only once
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def ask(question):

    client = chromadb.PersistentClient(
        path=DB_PATH
    )

    collection = client.get_collection(
        name=COLLECTION_NAME
    )

    query_embedding = embedding_model.encode(
        question,
        convert_to_numpy=True
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    citations = []
    context_parts = []

    for doc, meta in zip(
        documents,
        metadatas
    ):

        citation = (
            f"{meta['source']} "
            f"(Page {meta['page']})"
        )

        citations.append(citation)

        context_parts.append(
            f"[{citation}]\n{doc}"
        )

    context = "\n\n".join(
        context_parts
    )

    prompt = f"""
You are a document question-answering assistant.

Rules:
1. Use ONLY the provided context.
2. Do not use outside knowledge.
3. If the answer is not present in the context, reply exactly:
I cannot find the answer in the documents.
4. Mention source citations when possible.

Context:
{context}

Question:
{question}

Answer:
"""

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text, citations
import os
import chromadb

from sentence_transformers import SentenceTransformer

from document_loader import (
    load_pdf,
    load_docx,
    load_txt
)

from chunker import chunk_documents
from config import *


def load_all_documents():

    documents = []

    if not os.path.exists("data"):
        raise FileNotFoundError(
            "data folder not found"
        )

    for file in os.listdir("data"):

        path = os.path.join(
            "data",
            file
        )

        if file.endswith(".pdf"):
            documents.extend(
                load_pdf(path)
            )

        elif file.endswith(".docx"):
            documents.extend(
                load_docx(path)
            )

        elif file.endswith(".txt"):
            documents.extend(
                load_txt(path)
            )

    return documents


def build_db():

    docs = load_all_documents()

    if len(docs) == 0:
        print("No documents found")
        return

    chunks = chunk_documents(
        docs,
        CHUNK_SIZE,
        CHUNK_OVERLAP
    )

    print(f"Documents Loaded : {len(docs)}")
    print(f"Chunks Created   : {len(chunks)}")

    client = chromadb.PersistentClient(
        path=DB_PATH
    )

    try:
        client.delete_collection(
            COLLECTION_NAME
        )
    except:
        pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True
    ).tolist()

    print("Saving to ChromaDB...")

    collection.add(
        ids=[
            str(i)
            for i in range(len(chunks))
        ],
        embeddings=embeddings,
        documents=texts,
        metadatas=[
            chunk["metadata"]
            for chunk in chunks
        ]
    )

    print(
        f"Successfully indexed {len(chunks)} chunks."
    )


if __name__ == "__main__":
    build_db()
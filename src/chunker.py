def chunk_documents(
        docs,
        chunk_size=1000,
        overlap=200
):

    chunks = []

    for doc in docs:

        text = doc["text"]
        metadata = doc["metadata"]

        start = 0

        while start < len(text):

            end = min(
                start + chunk_size,
                len(text)
            )

            chunks.append({
                "text": text[start:end],
                "metadata": metadata
            })

            start += (
                chunk_size - overlap
            )

    return chunks
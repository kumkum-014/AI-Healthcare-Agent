from document_loader import load_pdfs
from chunker import split_text
from vector_db import collection


documents = load_pdfs()

for document in documents:

    chunks = split_text(document["text"])

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            metadatas=[
                {
                    "source": document["filename"]
                }
            ],
            ids=[
                f"{document['filename']}_{i}"
            ]
        )

print("Healthcare documents added successfully!")
print("Total chunks:", collection.count())
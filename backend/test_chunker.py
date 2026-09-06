from document_loader import load_pdfs
from chunker import split_text


documents = load_pdfs()


for document in documents:

    chunks = split_text(document["text"])

    print("\n================================")
    print("FILE:", document["filename"])
    print("NUMBER OF CHUNKS:", len(chunks))
    print("================================")

    for i, chunk in enumerate(chunks[:3]):

        print(f"\nCHUNK {i + 1}")

        print(chunk[:300])
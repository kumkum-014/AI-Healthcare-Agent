from document_loader import load_pdfs


documents = load_pdfs()


print("\n==============================")
print("TOTAL DOCUMENTS:", len(documents))
print("==============================\n")


for document in documents:

    print("FILE:", document["filename"])

    print("\nTEXT PREVIEW:")

    print(document["text"][:500])

    print("\n------------------------------\n")
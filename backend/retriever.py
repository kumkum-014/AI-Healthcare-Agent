from vector_db import collection


def search_knowledge(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    documents = results.get("documents", [[]])[0]

    return documents
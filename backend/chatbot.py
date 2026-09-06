from ollama import chat

from retriever import search_knowledge


def ask_healthcare_agent(question):

    # Search relevant information from healthcare PDFs
    documents = search_knowledge(question)

    # If nothing was found
    if not documents:
        return "I could not find relevant information in the healthcare knowledge base."

    # Combine retrieved documents
    context = "\n\n".join(documents)

    prompt = f"""
You are a simple healthcare educational assistant.

Answer the user's question using ONLY the information
provided in the healthcare knowledge base below.

Healthcare Knowledge Base:
{context}

User Question:
{question}

Rules:
- Give a simple and easy-to-understand answer.
- Do not diagnose diseases.
- Do not prescribe medicines.
- Do not invent medical information.
- If the answer is not available in the knowledge base,
  say that the information is not available in the provided documents.
- For serious or emergency symptoms, advise the user to
  contact a qualified healthcare professional.

Answer:
"""

    response = chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"] 
from rag.retriever import retrieve_documents
from ai.granite_model import generate_answer


def ask_assistant(question):

    documents = retrieve_documents(question)

    context = "\n\n".join(documents)

    prompt = f"""
You are a Utility AI Assistant.

Answer only using the provided context.

If the answer is not present in the context, say:
"I couldn't find that information in the knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer
    }
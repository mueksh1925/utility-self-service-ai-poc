import chromadb
from rag.embeddings import create_embedding

client = chromadb.PersistentClient(path="./vector-db")

collection = client.get_or_create_collection(
    name="utility-kb"
)

def retrieve_documents(question):

    query_vector = create_embedding(question)

    result = collection.query(
        query_embeddings=[query_vector],
        n_results=3
    )

    return result["documents"][0]
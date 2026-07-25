import chromadb


client = chromadb.PersistentClient(
    path="./vector-db"
)


collection = client.get_or_create_collection(
    name="utility-kb"
)


def add_document(
        doc_id,
        text,
        embedding):


    collection.add(

        ids=[doc_id],

        documents=[text],

        embeddings=[embedding]

    )
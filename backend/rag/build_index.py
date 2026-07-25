from document_loader import load_documents
from embeddings import create_embedding
from vector_store import add_document


docs = load_documents()


for index,doc in enumerate(docs):

    vector = create_embedding(
        doc["content"]
    )


    add_document(

        str(index),

        doc["content"],

        vector

    )


print(
"Vector Index Created"
)
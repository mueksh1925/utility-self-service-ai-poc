import chromadb

from rag.embeddings import create_embedding


client = chromadb.PersistentClient(
    path="./vector-db"
)


collection = client.get_or_create_collection(
    name="utility-kb"
)


documents = [
    {
        "id": "outage-policy",
        "text": """
        Customers can report electricity outage through mobile application,
        web portal, or customer support number.
        Outage status can be checked using customer account details.
        """
    },
    {
        "id": "billing-payment",
        "text": """
        Customers can view electricity bills, payment due dates,
        outstanding balance and payment history through the portal.
        """
    },
    {
        "id": "new-connection",
        "text": """
        Customers can request a new electricity connection online.
        Required documents include identity proof and address proof.
        """
    }
]


if __name__ == "__main__":

    for doc in documents:

        collection.upsert(
            ids=[
                doc["id"]
            ],

            documents=[
                doc["text"]
            ],

            embeddings=[
                create_embedding(doc["text"])
            ]
        )


    print("Utility KB indexed successfully")
from pathlib import Path


def load_documents():

    docs=[]

    path = Path(
        "../knowledge-base"
    )


    for file in path.rglob("*.md"):

        content = file.read_text()

        docs.append(
            {
             "file":str(file),
             "content":content
            }
        )

    return docs
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Utility AI Backend Running"
    }
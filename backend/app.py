from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import customer
from routes import billing
from routes import outage
from routes import service_request
from routes import assistant


app = FastAPI(
    title="Utility Self Service AI Backend",
    description="Mock APIs for IBM watsonx Assistant integration",
    version="1.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Routes
app.include_router(customer.router)
app.include_router(billing.router)
app.include_router(outage.router)
app.include_router(service_request.router)
app.include_router(assistant.router)


@app.get("/")
def home():
    return {
        "message": "Utility AI Backend Running"
    }
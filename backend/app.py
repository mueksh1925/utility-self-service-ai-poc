from fastapi import FastAPI

from routes import customer
from routes import billing
from routes import outage
from routes import service_request


app = FastAPI(
    title="Utility Self Service AI Backend",
    description="Mock APIs for IBM watsonx Assistant integration",
    version="1.0"
)


app.include_router(customer.router)
app.include_router(billing.router)
app.include_router(outage.router)
app.include_router(service_request.router)


@app.get("/")
def home():
    return {
        "message": "Utility AI Backend Running"
    }
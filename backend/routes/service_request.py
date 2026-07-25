from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter(
    prefix="/api/service-request",
    tags=["Service Request"]
)


@router.post("/")
def create_request(request: dict):

    ticket = "OUT-" + str(random.randint(10000, 99999))

    return {
        "ticketNumber": ticket,
        "createdDate": datetime.now(),
        "status": "Created",
        "request": request
    }
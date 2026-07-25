from fastapi import APIRouter
import json

router = APIRouter(
    prefix="/api/outages",
    tags=["Outage"]
)


@router.get("/{customer_id}")
def check_outage(customer_id: str):

    with open("data/outages.json") as file:
        outages = json.load(file)

    for outage in outages:

        if outage["customerId"] == customer_id:
            return outage

    return {
        "customerId": customer_id,
        "status": "NO_OUTAGE",
        "message": "No active outage found"
    }
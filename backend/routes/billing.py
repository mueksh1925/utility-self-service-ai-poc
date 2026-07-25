from fastapi import APIRouter
import json
router = APIRouter(
    prefix="/api/billing",
    tags=["Billing"]
)


@router.get("/{customer_id}")
def get_bill(customer_id: str):
    with open("data/bills.json") as file:
        bills=json.load(file)

    for bill in bills:
        if bill["customerId"] == customer_id:
            return bill

    return {
        "message":"Billing information not found"
    }
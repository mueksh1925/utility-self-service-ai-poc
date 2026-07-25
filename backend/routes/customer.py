from fastapi import APIRouter
import json

router = APIRouter(
    prefix="/api/customers",
    tags=["Customer"]
)


@router.get("/{customer_id}")
def get_customer(customer_id: str):

    with open("data/customers.json") as file:
        customers=json.load(file)

    for customer in customers:
        if customer["customerId"] == customer_id:
            return customer

    return {
        "message":"Customer not found"
    }
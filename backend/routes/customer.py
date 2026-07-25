from fastapi import APIRouter


router = APIRouter(
    prefix="/api/customers",
    tags=["Customer"]
)


@router.get("/{customer_id}")
def get_customer(customer_id: str):

    return {
        "customerId": customer_id,
        "name": "John Smith",
        "address": "123 Main Street",
        "serviceType": "Electricity",
        "status": "ACTIVE"
    }
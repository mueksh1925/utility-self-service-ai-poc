from fastapi import APIRouter

router = APIRouter(
    prefix="/api/billing",
    tags=["Billing"]
)


@router.get("/{customer_id}")
def get_bill(customer_id: str):
    return {
        "customerId": customer_id,
        "currentBill": 125.50,
        "dueDate": "2026-08-10",
        "paymentStatus": "PENDING"
    }
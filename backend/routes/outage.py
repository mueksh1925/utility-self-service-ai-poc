from fastapi import APIRouter

router = APIRouter(
    prefix="/api/outages",
    tags=["Outage"]
)


@router.get("/{zip_code}")
def check_outage(zip_code: str):

    return {
        "zipCode": zip_code,
        "outageStatus": "ACTIVE",
        "affectedCustomers": 350,
        "estimatedRestoration": "2026-07-26 18:00"
    }
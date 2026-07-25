from fastapi import APIRouter

router = APIRouter(
    prefix="/api/service-request",
    tags=["Service Request"]
)


@router.post("/")
def create_request(request: dict):

    return {
        "requestId": "SR10001",
        "status": "CREATED",
        "message": "Service request submitted successfully",
        "request": request
    }
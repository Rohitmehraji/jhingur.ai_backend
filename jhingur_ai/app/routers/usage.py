from fastapi import APIRouter

router = APIRouter()

@router.get("/usage")
def get_usage():
    return {"user_id": 1, "requests_made": 100, "requests_remaining": 900}

from fastapi import APIRouter

router = APIRouter()

@router.post("/subscribe")
def subscribe():
    return {"status": "success", "message": "You have successfully subscribed."}

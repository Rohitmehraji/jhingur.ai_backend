from fastapi import APIRouter

router = APIRouter()

@router.post("/inference")
def run_inference():
    return {"result": "This is a mock response from the AI/ML model."}

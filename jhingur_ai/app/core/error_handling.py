from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def http_exception_handler(request: Request, exc: Exception):
    logger.error(f"An error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred."},
    )

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, users, ml, payments, usage
from app.core.error_handling import http_exception_handler
from app.core.logging import setup_logging
from app.core.limiter import init_limiter


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_limiter()
    yield


app = FastAPI(lifespan=lifespan)

# CORS
origins = [
    "http://localhost:3000",
    "https://jhingur-ai-frontend.vercel.app",  # Assuming this is the frontend's production URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_logging()

app.add_exception_handler(Exception, http_exception_handler)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(ml.router, prefix="/ml", tags=["ml"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(usage.router, prefix="/usage", tags=["usage"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Jhingur.ai"}

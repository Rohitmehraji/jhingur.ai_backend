from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Jhingur.ai"
    DEBUG: bool = True

    DATABASE_URL: str

    OPENAI_API_KEY: str

    STRIPE_SECRET_KEY: str

    RAZORPAY_KEY_ID: str
    RAZORPAY_KEY_SECRET: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()

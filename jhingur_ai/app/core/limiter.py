from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
import os

async def init_limiter():
    if os.environ.get("TESTING") != "True":
        redis_connection = redis.from_url("redis://localhost:6379", encoding="utf-8")
        await FastAPILimiter.init(redis_connection)

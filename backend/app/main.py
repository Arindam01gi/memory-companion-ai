from fastapi import FastAPI
from contextlib import asynccontextmanager


from app.core.database import engine
from sqlalchemy import text




@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("✅ Database connected successfully")

    except Exception as e:
        print(f"❌ Database connection failed: {e}")

    yield


app = FastAPI(
    title="Memory Companion API",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def root():
    return {
        "message" : "Memory Companion API is running"
    }


@app.get("/health")
def health():
    return {
        "status" :"healthy"
    }
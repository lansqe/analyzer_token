from fastapi import FastAPI
from app.api.endpoints import router as api_router
from app.core.database import async_engine, Base

app = FastAPI(title="Token Analyzer", version="0.1.0")


app.include_router(api_router, prefix="/api")

async def init_models():
    """Инициализация моделей (для тестов/разработки)"""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    """Действия при запуске приложения"""
    await init_models()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
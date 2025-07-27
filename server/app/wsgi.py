from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.init_db import init_db
from app.api.v1.router.order import router as orders_router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的前端来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的请求头
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


# 注册路由
app.include_router(orders_router, prefix="/api/v1", tags=["orders"])


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}

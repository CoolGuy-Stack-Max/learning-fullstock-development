from typing import Generator
from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.session import SessionLocal
from app.services.order import OrderService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_order_service(db: Session = Depends(get_db)) -> OrderService:
    return OrderService(db)

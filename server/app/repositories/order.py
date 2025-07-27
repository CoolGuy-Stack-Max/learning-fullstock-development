from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate
from app.utils.pagination import Page


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, order_id: int) -> Order | None:
        return self.db.get(Order, order_id)

    def get_by_order_no(self, order_no: str) -> Order | None:
        stmt = select(Order).where(Order.order_no == order_no)
        return self.db.scalar(stmt)

    def list(self, skip: int = 0, limit: int = 50) -> list[Order]:
        stmt = select(Order).offset(skip).limit(limit)
        print(stmt)
        # return Page.create(total=len(list(self.db.scalars(stmt)), items=list(self.db.scalars(stmt))), page=1,size=20)
        return list(self.db.scalars(stmt))

    def create(self, data: OrderCreate) -> Order:
        obj = Order(**data.dict())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, db_obj: Order, data: OrderUpdate) -> Order:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(db_obj, field, value)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: Order) -> None:
        self.db.delete(db_obj)
        self.db.commit()

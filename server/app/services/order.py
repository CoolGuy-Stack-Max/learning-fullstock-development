from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.order import OrderRepository
from app.schemas.order import OrderCreate, OrderUpdate, OrderRead


class OrderService:
    def __init__(self, db: Session):
        self.repo = OrderRepository(db)

    def list_orders(self, skip: int = 0, limit: int = 50) -> list[OrderRead]:
        return self.repo.list(skip=skip, limit=limit)

    def get_order(self, order_id: int) -> OrderRead:
        obj = self.repo.get(order_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
            )
        return obj

    def create_order(self, data: OrderCreate) -> OrderRead:
        # 唯一性检查（order_no）
        if self.repo.get_by_order_no(data.order_no):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="order_no exists"
            )
        return self.repo.create(data)

    def update_order(self, order_id: int, data: OrderUpdate) -> OrderRead:
        obj = self.repo.get(order_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
            )
        return self.repo.update(obj, data)

    def delete_order(self, order_id: int) -> None:
        obj = self.repo.get(order_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
            )
        self.repo.delete(obj)

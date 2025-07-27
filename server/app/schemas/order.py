from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    order_no: str
    customer_name: str
    order_date: date


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: str | None = None
    order_date: date | None = None


class OrderRead(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


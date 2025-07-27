from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Date, DateTime

from app.db.base import Base


class Order(Base):
    __tablename__ = "admin_customer_orders"
    __table_args__ = {"schema": "public"} 

    id = Column(Integer, primary_key=True, index=True)
    order_no = Column(String(50), unique=True, index=True, nullable=False)
    customer_name = Column(String(100), nullable=False)
    order_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

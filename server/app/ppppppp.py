# server/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 示例订单数据
orders = [
    {"orderNo": "A001", "customerName": "张三", "orderDate": "2025-07-23"},
    {"orderNo": "A002", "customerName": "李四", "orderDate": "2025-07-24"},
]


# 请求数据模型
class Order(BaseModel):
    orderNo: str
    customerName: str
    orderDate: str


@app.get("/orders/", response_model=List[Order])
async def get_orders():
    return orders


@app.post("/orders/", response_model=Order)
async def create_order(order: Order):
    orders.append(order.dict())  # 保存新订单
    return order


@app.put("/orders/{order_no}", response_model=Order)
async def update_order(order_no: str, order: Order):
    for existing_order in orders:
        if existing_order["orderNo"] == order_no:
            existing_order.update(order.dict())  # 更新订单
            return existing_order
    return {"error": "Order not found"}


@app.delete("/orders/{order_no}", response_model=Order)
async def delete_order(order_no: str):
    for existing_order in orders:
        if existing_order["orderNo"] == order_no:
            orders.remove(existing_order)  # 删除订单
            return existing_order
    return {"error": "Order not found"}

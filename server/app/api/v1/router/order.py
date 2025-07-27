from fastapi import APIRouter, Depends, Query, status
from typing import List

from app.schemas.order import OrderCreate, OrderUpdate, OrderRead
from app.api.deps import get_order_service
from app.services.order import OrderService

router = APIRouter(prefix="/orders")


@router.get("/", response_model=List[OrderRead])
async def list_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    service: OrderService = Depends(get_order_service),
):
    return service.list_orders(skip=skip, limit=limit)


@router.get("/{order_id}", response_model=OrderRead)
async def get_order(order_id: int, service: OrderService = Depends(get_order_service)):
    return service.get_order(order_id)


@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
async def create_order(
    data: OrderCreate, service: OrderService = Depends(get_order_service)
):
    return service.create_order(data)


@router.put("/{order_id}", response_model=OrderRead)
async def update_order(
    order_id: int, data: OrderUpdate, service: OrderService = Depends(get_order_service)
):
    return service.update_order(order_id, data)


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order_id: int, service: OrderService = Depends(get_order_service)
):
    service.delete_order(order_id)
    return None

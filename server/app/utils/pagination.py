from typing import Any, Generic, List, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class Page(BaseModel, Generic[T]):
    total: int
    items: List[T]
    page: int
    size: int

    @staticmethod
    def create(total: int, items: List[T], page: int, size: int) -> "Page[T]":
        return Page(total=total, items=items, page=page, size=size)

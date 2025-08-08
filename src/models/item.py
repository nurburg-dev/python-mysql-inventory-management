from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    quantity: int
    price: float
    category: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CreateItemRequest(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    price: float
    category: Optional[str] = None

class TemporarilyBlockInventoryRequest(BaseModel):
    itemId: int
    quantity: int

class TemporarilyBlockInventoryResponse(BaseModel):
    blockId: int

class PermanentlyBlockInventory(BaseModel):
    blockId: int
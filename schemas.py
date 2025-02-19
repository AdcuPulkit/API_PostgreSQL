from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: int
    quantity: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase): 
    id: int
    
    class Config:
        from_attributes = True

# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# Pydantic model for an item
class Item(BaseModel):
    id: str
    name: str

# In-memory storage for items
items: List[Item] = []

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def add_item(name: str):
    if not name.strip():
        raise HTTPException(status_code=400, detail="Item name cannot be empty.")
    new_item = Item(id=str(uuid4()), name=name.strip())
    items.append(new_item)
    return new_item

@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: str):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return {"detail": "Item deleted successfully."}
    raise HTTPException(status_code=404, detail="Item not found.")

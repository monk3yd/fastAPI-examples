from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

# Inventory Management System Example
# https://www.youtube.com/watch?v=-ykeT6kk4bk
# https://fastapi.tiangolo.com/

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {}

# Path parameter(s) example
@app.get("/get-item/{item_id}")  # Endpoint
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view.", gt=0, lt=2)):
    return inventory[item_id]

# Query parameter(s) example
@app.get("/get-by-name")  # Endpoint
def get_name(uid: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found.")

# Path & Query parameter(s) example
@app.get("/get-by-brand/{item_id}")  # Endpoint
def get_brand(item_id: int, name: Optional[str] = None):
    if inventory[item_id]["name"] == name:
        return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item brand not found.")

# Request body parameter(s) example
@app.post("/create-item/{item_id}")  # Endpoint
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists.")
    
    # inventory[item_id] = {"name": item.name, "price": item.price, "brand": item.brand}
    # FastAPI converts Item object automatically into JSON since it inherits from BaseModel
    inventory[item_id] = item
    return inventory[item_id]

# PUT
# DELETE
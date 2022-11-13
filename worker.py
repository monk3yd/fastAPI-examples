from fastapi import FastAPI, Path
from typing import Optional

# Inventory Management System Example
# https://www.youtube.com/watch?v=-ykeT6kk4bk
# https://fastapi.tiangolo.com/

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

# Path parameter(s) example
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view.")):
    return inventory[item_id]

# Query parameter(s) example
@app.get("/get-by-name")
def get_name(uid: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not Found"}

# Path & Query parameter(s) example
@app.get("/get-by-brand/{item_id}")
def get_brand(item_id: int, name: Optional[str] = None):
    if inventory[item_id]["name"] == name:
        return inventory[item_id]
    return {"Data": "Not Found"}
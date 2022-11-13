from fastapi import FastAPI

# Inventory Management System Example
# https://www.youtube.com/watch?v=-ykeT6kk4bk

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

# Path parameter(s) example
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name: str):
    return inventory[item_id]
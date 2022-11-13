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

# Path parameter example
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
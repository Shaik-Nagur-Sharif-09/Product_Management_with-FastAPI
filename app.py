from fastapi import FastAPI
import database

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Product Management API"
    }

@app.get("/products")
def get_products():
    return database.get_all_products()


@app.get("/products/{name}")
def search_product(name: str):
    product = database.search_product(name)
    if product:
        return product
    return {
        "message": "Product not found!"
    }


@app.post("/products")
def add_product(
    name: str,
    brand: str,
    stock: int,
    category: str,
    price: float
):
    database.insert_product(
        name,
        brand,
        stock,
        category,
        price
    )
    return {
        "message": "Product added successfully!"
    }


@app.delete("/products/{name}")
def delete_product(name: str):
    result = database.delete_product(name)
    if result:
        return {
            "message": "Product deleted successfully!"
        }
    return {
        "message": "Product not found!"
    }


@app.put("/products/{name}/stock")
def update_stock(
    name: str,
    new_stock: int
):
    result = database.update_stock(
        name,
        new_stock
    )
    if result:
        return {
            "message": "Stock updated successfully!"
        }
    return {
        "message": "Product not found!"
    }

# database.py

# This acts as a temporary mock database stored in your computer's memory (List of Dicts)
PRODUCTS_DB = [
    {
        "name": "Galaxy S24",
        "brand": "Samsung",
        "stock": 15,
        "category": "Electronics",
        "price": 79999.00
    },
    {
        "name": "MacBook Air",
        "brand": "Apple",
        "stock": 8,
        "category": "Electronics",
        "price": 92000.00
    }
]

def get_all_products():
    """Returns all products from the list"""
    return PRODUCTS_DB

def search_product(name: str):
    """Searches for a product by name (Case-insensitive)"""
    for product in PRODUCTS_DB:
        if product["name"].lower() == name.lower():
            return product
    return None

def insert_product(name: str, brand: str, stock: int, category: str, price: float):
    """Adds a new product to the list"""
    new_product = {
        "name": name,
        "brand": brand,
        "stock": stock,
        "category": category,
        "price": price
    }
    PRODUCTS_DB.append(new_product)
    return True

def delete_product(name: str):
    """Deletes a product matching the given name"""
    for i, product in enumerate(PRODUCTS_DB):
        if product["name"].lower() == name.lower():
            PRODUCTS_DB.pop(i)
            return True
    return False

def update_stock(name: str, new_stock: int):
    """Updates the stock quantity of a specific product"""
    for product in PRODUCTS_DB:
        if product["name"].lower() == name.lower():
            product["stock"] = new_stock
            return True
    return False

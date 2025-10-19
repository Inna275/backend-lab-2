from app import app
from flask import request
from app.data import categories
import uuid


@app.post("/category")
def create_category():
    category_data = request.get_json()
    category_id = uuid.uuid4().hex
    category = {
        "id": category_id, 
        "name": category_data.get("name")
    }
    categories[category_id] = category
    return category


@app.get("/category")
def get_categories():
    return list(categories.values())


@app.delete("/category")
def delete_category():
    category_data = request.get_json()
    category_id = category_data.get("id")
    categories.pop(category_id, None)
    return {"message": "Category deleted"}

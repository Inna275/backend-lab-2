from app import app
from flask import request
from app.data import users
import uuid


@app.post("/user")
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {
        "id": user_id,
        "name": user_data.get("name")
    }
    users[user_id] = user
    return user


@app.get("/users")
def get_users():
    return list(users.values())


@app.get("/user/<user_id>")
def get_user(user_id):
    return users.get(user_id, {})


@app.delete("/user/<user_id>")
def delete_user(user_id):
    users.pop(user_id, None)
    return {"message": "User deleted"}

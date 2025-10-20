from app import app
from flask import request
from app.data import records
from datetime import datetime
import uuid


@app.post("/record")
def create_record():
    record_data = request.get_json()
    record_id = uuid.uuid4().hex
    record = {
        "id": record_id,
        "user_id": record_data.get("user_id"),
        "category_id": record_data.get("category_id"),
        "created_at": datetime.utcnow().isoformat() + "Z",
        "amount": record_data.get("amount")
    }
    records[record_id] = record
    return record


@app.get("/record/<record_id>")
def get_record(record_id):
    return records.get(record_id, {})


@app.get("/record")
def get_records():
    user_id = request.args.get("user_id")
    category_id = request.args.get("category_id")

    if not user_id and not category_id:
        return {"message": "Provide user_id or category_id"}

    filtered = []
    for r in records.values():
        if user_id and category_id:
            if r["user_id"] == user_id and r["category_id"] == category_id:
                filtered.append(r)
        elif user_id and r["user_id"] == user_id:
            filtered.append(r)
        elif category_id and r["category_id"] == category_id:
            filtered.append(r)
    return filtered


@app.delete("/record/<record_id>")
def delete_record(record_id):
    records.pop(record_id, None)
    return {"message": "Record deleted"}

# ...existing code...
from flask import Blueprint, request, jsonify
from models import orders
from datetime import datetime
import json

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/api/orders', methods=["POST"])
def create_order():
    if request.is_json:
        data = request.get_json()
    else:
        data = {
            "customer": request.form.get("customer"),
            "items": request.form.get("items")
        }
    # nếu items là chuỗi JSON, cố parse
    if isinstance(data.get("items"), str):
        try:
            data["items"] = json.loads(data["items"])
        except:
            pass
    data["createdAt"] = datetime.utcnow()
    orders.insert_one(data)
    return jsonify({"message": "Đã tạo đơn hàng"}), 201

@order_bp.route('/api/orders', methods=["GET"])
def get_orders():
    raw = list(orders.find({}, {"_id": 0}).sort("createdAt", -1))
    for r in raw:
        if "createdAt" in r and hasattr(r["createdAt"], "isoformat"):
            r["createdAt"] = r["createdAt"].isoformat()
    return jsonify(raw), 200
# ...existing code...
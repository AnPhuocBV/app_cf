# ...existing code...
from flask import Blueprint, request, jsonify
from models import categories

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/api/categories', methods=["POST"])
def add_category():
    if request.is_json:
        data = request.get_json()
    else:
        data = {
            "name": request.form.get("name"),
            "price": request.form.get("price"),
            "image": request.form.get("image"),
            "description": request.form.get("description")
        }
    if not data.get("name"):
        return jsonify({"error": "Missing name"}), 400
    categories.insert_one(data)
    return jsonify({"message": "Đã thêm danh mục"}), 201

@category_bp.route('/api/categories', methods=["GET"])
def get_categories():
    result = list(categories.find({}, {"_id": 0}))
    return jsonify(result), 200

@category_bp.route('/api/categories', methods=["DELETE"])
def delete_category():
    if request.is_json:
        data = request.get_json()
    else:
        data = {"name": request.form.get("name")}
    name = data.get("name")
    if not name:
        return jsonify({"error": "Missing name"}), 400
    res = categories.delete_one({"name": name})
    if res.deleted_count == 0:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Đã xóa danh mục"}), 200
# ...existing code...
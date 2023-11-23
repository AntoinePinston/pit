"""Main module for the streamlit app"""
from flask import Flask, jsonify, request

from app.services.user_service import USERSERVICE

app = Flask(__name__)


@app.route("/users", methods=["GET"])
async def get_all_users():
    """Get all users"""

    users = await USERSERVICE.get_all()

    return jsonify([user.__dict__ for user in users]), 200


@app.route("/users/<user_id>", methods=["GET"])
async def get_user(user_id):
    """Get a single user by id"""

    user_id_int = int(user_id)
    user = await USERSERVICE.get_by_id(user_id_int)

    return jsonify(user.__dict__), 200


@app.route("/users", methods=["POST"])
async def create_user():
    """Create a new user"""
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email required"}), 400

    user = await USERSERVICE.create(data)

    return jsonify(user.__dict__), 201


@app.route("/users/<user_id>", methods=["PUT"])
async def update_user(user_id):
    """Update an existing user"""
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email required"}), 400

    user_id_int = int(user_id)
    user = await USERSERVICE.update(user_id_int, data)
    return jsonify(user.__dict__), 200


@app.route("/users/<user_id>", methods=["DELETE"])
async def delete_user(user_id):
    """Delete a user"""

    user_id_int = int(user_id)
    await USERSERVICE.delete(user_id_int)

    return "", 204

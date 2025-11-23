from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}   # {id: {"name": "", "email": ""}}

# Home
@app.route("/")
def home():
    return jsonify({"message": "User API is running"}), 200


# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# GET single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404


# POST create user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid data"}), 400

    user_id = len(users) + 1
    users[user_id] = {"name": data["name"], "email": data["email"]}

    return jsonify({"message": "User created", "id": user_id}), 201


# PUT update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id].update(data)

    return jsonify({"message": "User updated", "user": users[user_id]}), 200


# DELETE user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)

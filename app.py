import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"), serverSelectionTimeoutMS=5000)
db = client["flask_assignment"]
collection = db["submissions"]


@app.route("/api")
def api():
    file_path = os.path.join(app.root_path, "data.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.form or request.get_json(silent=True) or {}
    item_name = data.get("itemName", "").strip()
    item_description = data.get("itemDescription", "").strip()

    if not item_name or not item_description:
        return jsonify({"error": "itemName and itemDescription are required"}), 400

    try:
        db["todo_items"].insert_one({"itemName": item_name, "itemDescription": item_description})
        return jsonify({"message": "To-Do item saved successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Could not save item: {e}"}), 500


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            return render_template("form.html", error="Name and email are required")

        try:
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except Exception as e:
            return render_template("form.html", error=f"Could not save data: {e}")

    return render_template("form.html")


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)
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
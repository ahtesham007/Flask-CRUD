from flask import Flask, Response, request, url_for, jsonify
from flask_pymongo import PyMongo
import json
from pymongo.collection import Collection, ReturnDocument
from datetime import datetime
import os
from pymongo.errors import DuplicateKeyError
from models.model import User
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("DB_URI")
mongodb_client = PyMongo(app)
user_collection = mongodb_client.db.users

@app.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e):
    """
    An error-handler to ensure that MongoDB duplicate key errors are returned as JSON.
    """
    return jsonify(error=f"Duplicate key error."), 400

@app.route("/")
def health_check():
    return Response(response=json.dumps({"message": "server is up and running"}),
                    status=200,
                    mimetype='application/json')


@app.route("/users/", methods=["GET", "POST"])
def get_users():

    if request.method == "GET":
        users = user_collection.find({})
        user = [ {item: data[item] for item in data if item != '_id'} for data in users ]
        print(user)
        return Response(response=json.dumps(user),
                        status=200,
                        mimetype='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
    
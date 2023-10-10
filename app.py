from flask import Flask, Response, request, jsonify
from flask_pymongo import PyMongo, ObjectId
import json
import os
import flask
from datetime import datetime
from pymongo.errors import DuplicateKeyError
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "/api/v1"

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


@app.route(f"{BASE_URL}/")
def health_check():
    return Response(response=json.dumps({"message": "server is up and running"}),
                    status=200,
                    mimetype='application/json')


@app.route(f"{BASE_URL}/users/", methods=["GET", "POST", "PUT", "DELETE"])
def users_api():
    if request.method == "GET":
        try:
            users = user_collection.find()
            user = [{item: str(data[item])
                     for item in data if item != '_id'} for data in users]
            return Response(response=json.dumps(user),
                            status=200,
                            mimetype='application/json')

        except:
            flask.abort(400, "Not Found")

    elif request.method == "POST":
        try:
            payload = request.get_json()
            payload["created_date"] = datetime.utcnow()
            response = user_collection.insert_one(payload)
            output = {'message': 'Successfully Inserted',
                      'Document_ID': str(response.inserted_id)}

            return Response(response=json.dumps(output),
                            status=201,
                            mimetype='application/json')

        except:
            flask.abort(301, "Insertion failed")

    elif request.method == "PUT":

        try:
            payload = request.get_json()
            payload["data"]["updated_date"] = datetime.utcnow()
            updated_data = {"$set": payload['data']}
            user_id = payload["id"]
            user_id_obj = ObjectId(user_id)
            response = user_collection.update_one({"_id": user_id_obj}, updated_data)
            output = {'message': 'Successfully Updated' if response.modified_count >
                      0 else "Nothing was updated."}
            return Response(response=json.dumps(output),
                            status=202,
                            mimetype='application/json')

        except:
            flask.abort(403, "No Content")

    elif request.method == "DELETE":
        try:

            payload = request.get_json()
            filt = payload["filter"]
            response = user_collection.delete_one(filt)
            output = {'message': 'Successfully Deleted' if response.deleted_count >
                      0 else "Document not found."}
            return Response(response=json.dumps(output),
                            status=200,
                            mimetype='application/json')

        except:
            flask.abort(500, "Internal Server Error")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)

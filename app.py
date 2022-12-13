from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/")
def health_check():
    return Response(response=json.dumps({"message": "server is up and running"}),
                    status=200,
                    mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
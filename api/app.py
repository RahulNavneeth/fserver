from flask import Flask, request
from flask_cors import CORS
from gradio_client import Client

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello():
    if request.method == "GET":
        return "Hello World!"


@app.route("/api/cimta", methods=["POST"])
def cimta():
    if request.method == "POST":
        num_patients, avg_wait_time, distance_to_hospital, doc_rating = (
            request.json["num_patients"],
            request.json["avg_wait_time"],
            request.json["distance_to_hospital"],
            request.json["doc_rating"],
        )
        client = Client("aswatht/cimta")
        result = client.predict(
            num_patients,
            avg_wait_time,
            distance_to_hospital,
            doc_rating,
            api_name="/predict",
        )
        return result


if __name__ == "__main__":
    app.run()

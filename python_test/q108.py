from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/data", methods=["POST"])
def data():
    data = request.get_json()
    return jsonify(data)
if __name__ == "__main__":
    app.run()

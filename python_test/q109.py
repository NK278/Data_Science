from flask import Flask, send_from_directory
app = Flask(__name__)
@app.route("/static/<path:filename>")
def static_file(filename):
    return send_from_directory("static", filename)
if __name__ == "__main__":
    app.run()
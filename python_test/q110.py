from flask import Flask, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return redirect("/hello")
@app.route("/hello")
def hello():
    return "Hello, World!"
if __name__ == "__main__":
    app.run()
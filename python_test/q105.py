from flask import Flask, render_template
app = Flask(__name__)
@app.route("/names1")
def names():
    names = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    return render_template("names1.html", names=names)
if __name__ == "__main__":
    app.run()
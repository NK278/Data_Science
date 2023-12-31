from flask import Flask, render_template
app = Flask(__name__)
@app.route("/names")
def names():
    names = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    return render_template("names.html", names=names)
if __name__ == "__main__":
    app.run()
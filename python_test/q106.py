from flask import Flask, render_template
app = Flask(__name__)
@app.route("/names2")
def names():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("names2.html", names=names)
if __name__ == "__main__":
    app.run()
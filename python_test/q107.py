from flask import Flask, render_template
app = Flask(__name__)
@app.route("/names3")
def names():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("names3.html", names=names)
if __name__ == "__main__":
    app.run()
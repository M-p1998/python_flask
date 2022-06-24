from distutils.log import debug
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def fruit():
    return render_template("index.html")

@app.route("/buy", methods=["post"])
def form():
    print(request.form)
    # name=request.form("name")
    return redirect("/checkout")

@app.route("/checkout")
def checkout():
    print("showing")
    print(request.form)
    return render_template("fruits.html")
if __name__ == "__main__":
    app.run(debug=True)
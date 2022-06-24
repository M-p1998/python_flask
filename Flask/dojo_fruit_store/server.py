from distutils.log import debug
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "very secret dfaerhfdnkajihuerkjeor"

@app.route("/")
def fruit():
    return render_template("index.html")

@app.route("/buy", methods=["post"])
def form():
    print(request.form)
    
    session["userName"] = request.form["name"]
    session["userId"] = request.form["ID"]
    return redirect("/checkout")

@app.route("/checkout")
def checkout():
    print("showing")
    print(request.form)
    return render_template("fruits.html", )
if __name__ == "__main__":
    app.run(debug=True)
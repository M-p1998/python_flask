from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def first():
    return render_template("second.html" , times=3, colorBox="blue")

@app.route("/play/<int:x>")
def second(x):
    return render_template("second.html", times=x , colorBox="blue")

@app.route("/play/<int:y>/<string:color>")
def third(y, color):
    return render_template("second.html", times=y, colorBox=color)

if __name__ == "__main__":
    app.run(debug=True)
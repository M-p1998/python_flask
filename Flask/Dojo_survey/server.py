
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "dadhuaji9ue89rijkdosp0upowe"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit_form", methods=["post"])
def submit():
    session["Y_name"] = request.form["Name"]
    session["dojo_loc"] = request.form["location"]
    session["fav_lang"] = request.form["language"]
    session["comment(optional)"] = request.form["comment"]
    print(request.form)
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)

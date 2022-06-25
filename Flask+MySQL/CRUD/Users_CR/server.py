from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route("/")
def first():
    Many_users = User.get_all()
    print(Many_users)
    return render_template("read.html", userss = Many_users)

@app.route("/create_user", methods=["post"])
def create():
    data = {
        "fName": request.form["fName"],
        "lName": request.form["lName"],
        'email': request.form["email"]
    }
    User.save(data)
    print(User)
    return redirect("/")

@app.route("/users/new")
def new():
    return render_template("/create.html")

if __name__ =="__main__":
    app.run(debug=True)
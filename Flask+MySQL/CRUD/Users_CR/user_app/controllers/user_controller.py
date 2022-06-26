from user_app import app
from flask import Flask, render_template, request, redirect
from user_app.models.user import User
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
    return render_template("create.html")

@app.route("/users/<int:user_id>")
def show_one_user(user_id):
    data={
        "id": user_id
    }
    one_user = User.get_one(data)
    return render_template("one.html", aUser = one_user)

@app.route("/users/<int:user_id>/edit")
def edit(user_id): 
    data={ 
        "id": user_id
    }
    USER = User.get_one(data)
    return render_template("edit.html", USER1 =USER)

@app.route("/users/<int:user_id>/update", methods=["post"])
def update(user_id): 
    data={ 
        "id": user_id,
        "fName": request.form["fName"],
        "lName": request.form["lName"],
        "email": request.form["email"]
    }
    user =  User.update(data)
    print(user)
    return redirect(f"/users/{user_id}" )

@app.route("/users/<int:user_id>/delete")
def delete(user_id):
    data={
        "id": user_id
    }
    User.delete(data)
    return redirect("/")
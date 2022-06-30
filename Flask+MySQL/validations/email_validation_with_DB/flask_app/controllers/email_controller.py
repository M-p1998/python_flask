from flask_app import app
from flask import render_template, redirect,request
from flask_app.models.email import Email

@app.route("/")
def first():
    return render_template("email.html")

@app.route("/create/email", methods=["post"])
def second():
    if not Email.validate_email(request.form):
        return redirect("/")
    data={
        "EMAIL": request.form["EMAIL"]
    }
    Email.create(data)
    return redirect("/success")

@app.route("/success")
def third():
    all = Email.get_all()
    return render_template("success.html", all=all)

@app.route("/delete/<int:id>")
def delete(id):
    data={
        "id": id
    }
    Email.delete_email(data)
    return redirect("/success")

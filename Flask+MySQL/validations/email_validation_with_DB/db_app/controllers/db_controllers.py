from db_app import app
from flask import render_template, redirect, session, flash, request

@app.route("/")
def first():
    return render_template("email.html")
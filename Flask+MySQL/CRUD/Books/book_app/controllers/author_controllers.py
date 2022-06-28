from flask import Flask, redirect, render_template, request
from book_app import app
from book_app.models.author import Author


@app.route("/authors")
def index():
    Author.get_all_authors()
    return render_template("authors.html")

@app.route("/create/author", methods=["post"])
def create_author():
    data={
        "Name": request.form["Name"]
    }
    Author.create_authors(data)
    Author.get_all_authors()
    # print (data)
    print (request.form)
    return redirect("/authors")
from flask import Flask, redirect, render_template, request
from book_app import app
from book_app.models.author import Author
from book_app.models.book import Book


@app.route("/authors")
def index():
    authors = Author.get_all_authors()
    return render_template("authors.html", all_authors=authors)

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

@app.route("/authors/<int:author_id>")
def show(author_id):
    data={
        "id": author_id
    }
    books = Book.get_all_books()
    return render_template("author_show.html", books=books)
from flask import Flask, redirect, render_template, request
from book_app import app
from book_app.models.book import Book
from book_app.models.author import Author

@app.route("/books")
def book():
    book = Book.get_all_books()
    return render_template("books.html", books= book)

@app.route("/create/book", methods=["post"])
def create_Book():
    data={
        "Title": request.form["Title"],
        "Num": request.form["Num"]
    }
    Book.create_book(data)
    return redirect("/books")

@app.route("/books/<int:book_id>")
def show_book(book_id):
    DATA= {
        "id": book_id
    }
    authors = Author.get_all_authors()
    book = Book.get_book_by_id(DATA)
    return render_template("book_show.html", book2=book, all_authors=authors)

@app.route("/add/author", methods=["post"])
def add():
    data={
        "BOOK_ID":request.form["BOOK_ID"],
        "AUTHOR_ID":request.form["AUTHOR_ID"]

    }
    Book_id = request.form["BOOK_ID"]
    return redirect(f"/books/{Book_id}")
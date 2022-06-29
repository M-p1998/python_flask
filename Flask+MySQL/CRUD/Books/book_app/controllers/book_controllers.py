from flask import Flask, redirect, render_template, request
from book_app import app
from book_app.models.book import Book

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
from sqlite3 import connect
from book_app.config.mysqlconnection import connectToMySQL
from book_app.models import author
class Book:
    def __init__(self, data):
        self.id=data["id"]
        self.title=data["title"]
        self.number_of_pages=data["number_of_pages"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

        self.authors_who_favorited = []
    @classmethod
    def create_book(cls, data):
        query="INSERT INTO books (title, number_of_pages, created_at, updated_at) VALUES (%(Title)s, %(Num)s, NOW(), NOW());"
        return connectToMySQL("authors_books").query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query="SELECT * FROM books;"
        results = connectToMySQL("authors_books").query_db(query)
        bookss=[]
        for book in results:
            bookss.append(cls(book))
        return bookss

    @classmethod
    def get_book_by_id(cls, data):
        query="SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id  = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL("authors_books").query_db(query,data)
        oneBook = cls(results[0])
        for row in results:
            if row["authors.id"] == None:
                break;
            author_data={
                "id": row["authors.id"],
                "name":row["name"],
                "created_at": row["authors.created_at"],
                "updated_at":row["authors.updated_at"]
            }
            oneBook.authors_who_favorited.append(author.Author(author_data))
        return oneBook
    
    @classmethod
    def unfavorited_books(cls, data):
        query="SELECT * FROM books WHERE books.id NOT IN (SELECT book_id from favorites WHERE author_id =%(id)s);"
        results = connectToMySQL("authors_books").query_db(query,data)
        books=[]
        for b in results:
            books.append(cls(b))
        return books
    
    
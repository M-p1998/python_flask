
from book_app.config.mysqlconnection import connectToMySQL
from book_app.models import book

class Author:
    def __init__(self, data):
        self.id= data["id"]
        self.name=data["name"]
        self.created_at= data["created_at"]
        self.updated_at=data["updated_at"]

        self.many_books = []

    @classmethod
    def create_authors(cls, data):
        query= "INSERT INTO authors (name, created_at, updated_at) VALUES (%(Name)s, NOW(), NOW());"
        return connectToMySQL("authors_books").query_db(query, data)
    
    @classmethod
    def get_all_authors(cls):
        query="SELECT * FROM authors;"
        results= connectToMySQL("authors_books").query_db(query)
        authors=[]
        for a in results:
            authors.append(cls(a))
        return authors

    @classmethod
    def get_author_by_id(cls,data):
        query="SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id  = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL("authors_books").query_db(query,data)
        author = cls(results[0])
        for db in results:
            if db["books.id"] == None:
                break;
            book_data = {
                "id": db["books.id"],
                "title": db["title"],
                "number_of_pages": db["number_of_pages"],
                "created_at": db["books.created_at"],
                "updated_at": db["books.updated_at"]
            }
            author.many_books.append(book.Book(book_data))
        return author

    @classmethod
    def add_book_to_authors_fav(cls, data):
        query="INSERT INTO favorites (book_id,author_id) VALUES (%(BOOK_id)s, %(Author_id)s);"
        return connectToMySQL("authors_books").query_db(query,data)

    @classmethod
    def unfav_author(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id from favorites WHERE book_id =%(id)s);"
        results = connectToMySQL("authors_books").query_db(query,data)
        authors= []
        for a in results:
            authors.append(cls(a))
        return authors

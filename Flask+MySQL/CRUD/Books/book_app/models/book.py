from book_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id=data["id"]
        self.title=data["title"]
        self.number_of_pages=data["number_of_pages"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

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
    
    
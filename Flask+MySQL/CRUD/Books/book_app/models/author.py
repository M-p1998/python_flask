
from book_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id= data["id"]
        self.name=data["name"]
        self.created_at= data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def create_authors(cls, data):
        query= "INSERT INTO authors (name, created_at, updated_at) VALUES (%(Name)s, NOW(), NOW());"
        return connectToMySQL("authors_books").query_db(query, data)
    
    classmethod
    def get_all_authors(cls):
        query="SELECT * FROM authors;"
        results= connectToMySQL("authors_books").query_db(query)
        authors=[]
        for a in results:
            authors.append(cls(a))
        return authors
from dojos_ninjas.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_ninja(cls, data):
        query="INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fName)s, %(lName)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL("dojos_ninjas").query_db(query, data)

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM dojos;"
        results=connectToMySQL("dojos_ninjas").query_db(query)
        ninjas=[]
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
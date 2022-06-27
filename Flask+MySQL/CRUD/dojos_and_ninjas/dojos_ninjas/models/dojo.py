from dojos_ninjas.config.mysqlconnection import connectToMySQL
from dojos_ninjas.models import ninja
class Dojo:
    def __init__(self,data):
        self.id=data["id"]
        self.name=data["name"]
        self.created_at=data["created_at"]
        self.updated_at = data["updated_at"]
        
        self.ninjas = []
    
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(NAME)s, NOW(), NOW()); "
        return connectToMySQL("dojos_ninjas").query_db(query,data)

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_ninjas").query_db(query)
        dojos=[]
        for one_dojo in results:
            dojos.append(cls(one_dojo))
        return dojos

    classmethod
    def get_one_dojo(cls, data):
        query="SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_ninjas").query_db(query, data)
        return (cls(results[0]))

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_ninjas").query_db(query,data)
        dojo = cls(results[0])
        for all in results:
            ninjas_data={
                "id": all["ninjas.id"],
                "first_name": all["first_name"],
                "last_name": all["last_name"],
                "age": all["age"],
                "dojo_id": all["dojo_id"],
                "created_at": all["created_at"],
                "updated_at": all["updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninjas_data))
        return dojo

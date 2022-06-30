from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash

class Email:
    def __init__(self,data):
        self.id=data["id"]
        self.email_address=data["email_address"]
        self.created_at=data["created_at"]
        self.updated_at= data["updated_at"]

    @classmethod
    def create(self,data):
        query= "INSERT INTO emails (email,created_at,updated_at) VALUES (%(EMAIL)s, NOW(), NOW());"
        return connectToMySQL("email_db").query_db(query,data)

    @staticmethod
    def validate_email(emaIL):
        is_valid=True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(emaIL["EMAIL"]): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
 
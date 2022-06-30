from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash

class Email:
    def __init__(self,data):
        self.id=data["id"]
        self.email=data["email"]
        self.created_at=data["created_at"]
        self.updated_at= data["updated_at"]

    @classmethod
    def create(self,data):
        query= "INSERT INTO emails (email,created_at,updated_at) VALUES (%(EMAIL)s, NOW(), NOW());"
        return connectToMySQL("email_db").query_db(query,data)

    # @staticmethod
    # def validate_email(emaIL):
    #     is_valid=True
    #     if len(emaIL["EMAIL"])==0:
    #         flash("Email must be entered.")
    #         is_valid = False
    #     elif len(emaIL["EMAIL"])< 8:
    #         flash("Email must be at least 8 characters long.")
    #         is_valid = False
    #     # elif len(emaIL) ==  emaIL["EMAIL"]:
    #     #     flash("That email is already taken.")
    #     #     is_valid = False
    #     elif len(emaIL) >= 1:
    #         flash("Email already taken.")
    #         is_valid=False
    #     elif not EMAIL_REGEX.match(emaIL["EMAIL"]): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     return is_valid

    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(EMAIL)s;"
        results = connectToMySQL("email_db").query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        elif not EMAIL_REGEX.match(email['EMAIL']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid

    @classmethod
    def get_all(cls):
        query="SELECT * FROM emails;"
        results = connectToMySQL("email_db").query_db(query)
        EMAILS=[]
        for db in results:
            EMAILS.append(cls(db))
        return EMAILS

    @classmethod
    def delete_email(cls,data):
        query ="DELETE FROM emails WHERE emails.id = %(id)s;"
        return connectToMySQL("email_db").query_db(query,data)

    
 
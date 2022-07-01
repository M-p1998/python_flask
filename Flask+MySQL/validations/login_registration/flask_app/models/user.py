
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL("login_registration").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(Email)s;"
        results = connectToMySQL("login_registration").query_db(query,data)
        print(results)
        if len(results) == 0:
            return False    
        else:
            return cls(results[0])

    @classmethod
    def register_user(cls, data):
        query= "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (%(Fname)s,%(Lname)s,%(Email)s,%(Password)s,NOW(),NOW());"
        results = connectToMySQL("login_registration").query_db(query,data)
        return results

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data["Fname"]) <2:
            flash("First name must be at least 2 characters.","register")
            is_valid = False

        if len(data["Lname"]) <2:
            flash("Last name must be at least 2 characters.","register")
            is_valid = False

        if len(data["Email"]) == 0:
            flash("Email must be entered.","register")
            is_valid = False
        elif not EMAIL_REGEX.match (data["Email"]):
            flash("Invalid email address!","register")
            is_valid = False

        # validation on passwords to have a least 1 number and 1 uppercase letter
        # elif not data["password"].isdigit():
        #     flash("Your password has a number in it.")
        #     is_valid=False
        # elif not len(data["password"]).isupper():
        #     flash("Your password has a capital letter in it.")
        #     is_valid=False

        if len(data["Password"]) <8:
            flash("Password must be at least 8 characters.","register")
            is_valid = False

        if data['Password'] != data["confirm_password"]:
            flash("Your passwords do not match.","register") 
            is_valid = False

        query = "SELECT * FROM users WHERE email = %(Email)s;"
        results = connectToMySQL("login_registration").query_db(query,data)
        print(f"results:{results}")
        # we do not expect anything to be inside of result.
        if len(results) >= 1:
            flash("That email is already taken!","register")
            is_valid =False
        return is_valid

    @classmethod
    def login_user(cls,data):
        query="INSERT INTO users (email,password) VALUES (%(Email)s,%(Password)s);"
        results = connectToMySQL("login_registration").query_db(query,data)
        return results

    @staticmethod
    def validate_login(data):
        is_valid = True
        # if len(data["email"]) == 0:
        #     flash("Email is required", "login")
        #     is_valid = False
        # if len(data["email"]) == 0:
        #     flash("Password is required", "login")
        #     is_valid = False
        return is_valid

    

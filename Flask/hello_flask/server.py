from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/success")
def success():
    return "success"

@app.route("/hello/<name>")
def hello(name):
    print(name)
    return "Hello, " + name

@app.route("/users/<string:username>/<int:id>")
def show_user_profile(username, id):
    print(username,id)
    # return "username: " + username + ", " + "id: " + id
    return f"username: {username  * id }  "

@app.route("/lists")
def render_lists():
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John' , 'age' : 39},
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", students = student_info, random_numbers=[3,1,5])

if __name__=="__main__":
    app.run(debug=True)
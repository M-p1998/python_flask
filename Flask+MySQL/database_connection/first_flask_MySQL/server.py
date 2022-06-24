
from flask import Flask, render_template, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", my_friends=friends)

@app.route("/create_friend", methods=["post"])
def create_friend():
    data={
        "fname": request.form["fname"],
        "lname":request.form["lname"],
        "occ": request.form["occ"]
    }
    
    Friend.save(data)
    print(request.form)
    return redirect("/")
            
if __name__ == "__main__":
    app.run(debug=True)
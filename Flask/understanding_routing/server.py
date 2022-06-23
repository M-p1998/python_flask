from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo1():
    return "Dojo!"

@app.route("/say/<string:name>")
# @app.route("/say/<:name>")
def say_name(name):
    print(name)
    # return f"Hi {name}!"
    return "Hi " + name

@app.route("/repeat/<int:id>/<string:name>")
def repeat(id, name):
    return f" {name * id}"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
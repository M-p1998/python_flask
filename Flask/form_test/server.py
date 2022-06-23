from flask import Flask, render_template, redirect, request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/users", methods=["post"])
def user():
    print("Got Post Info")
    print(request.form)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
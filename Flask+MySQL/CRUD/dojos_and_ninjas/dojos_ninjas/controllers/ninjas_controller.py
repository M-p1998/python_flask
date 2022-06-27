from dojos_ninjas import app
from flask import redirect, render_template, request
from dojos_ninjas.models.dojo import Dojo
from dojos_ninjas.models.ninja import Ninja

@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", DOJOS = dojos)

@app.route("/create/ninjas", methods=["post"])
def create_ninja():
    data={
        "fName": request.form["fName"],
        "lName": request.form["lName"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.create_ninja(data)
    print(request.form)
    dojosss_id = request.form["dojo_id"]
    return redirect(f"/dojos/{dojosss_id}")

@app.route("/dojos/<int:dojoId>")
def one(dojoId):
    data={
        "id": dojoId
    }
    
    d_n = Dojo.get_dojo_with_ninjas(data)
    
    return render_template("dojo_show.html",  all= d_n)

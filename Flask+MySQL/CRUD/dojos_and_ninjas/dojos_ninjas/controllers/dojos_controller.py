from flask import Flask, request, redirect, render_template
from dojos_ninjas import app
from dojos_ninjas.models.dojo import Dojo

@app.route("/dojos")
def dojos():
    dojos=Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos= dojos)

@app.route("/create/dojos", methods=["post"])
def create_dojo():
    data_from_database={
        "NAME": request.form["NAME"]
    }
    print(data_from_database)
    dojos=Dojo.get_all_dojos()
    print(dojos)
    Dojo.create_dojo(data_from_database)
    
    return redirect("/dojos")
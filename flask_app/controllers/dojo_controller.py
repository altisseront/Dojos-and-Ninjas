from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def redir():
    return redirect('/dojos')

@app.route('/dojos')
def displaydojos():
    return render_template('index.html', dojos = Dojo.get_all())

@app.route('/ninjas')
def ninja():
    return render_template('newninja.html', dojos = Dojo.get_all())

@app.route('/create_ninja', methods=['POST'])
def createNinja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"]
        }
    Ninja.create(data)
    return redirect('/dojos/'+ data["dojo_id"])
@app.route('/dojos/<int:dojo_id>')
def showDojo(dojo_id):
    data = {
        "id": dojo_id
    }    
    return render_template('thisdojo.html', ninjas = Ninja.get_ninjas_with_dojo(data), dojoname = Dojo.get_dojo_name(data))

@app.route('/create_dojo', methods = ['POST'])
def createDojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.create(data)
    return redirect('/dojos')
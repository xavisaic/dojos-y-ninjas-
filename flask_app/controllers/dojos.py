from flask import render_template,request,redirect
from flask_app import app
# ...server.py
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/')
def index():
    all_dojos=Dojo.get_all()
    return render_template("add_dojo.html", all_dojos=all_dojos)

@app.route('/createdojo',methods=['POST'])
def create_dojo():
    data = {
        "name":request.form['name']
    }
    Dojo.save(data)
    
    return redirect('/')

# @app.route('/show')
# def show_dojos():
#     all_dojos=Dojo.get_all()
#     return render_template("show", all_dojos=all_dojos)


@app.route('/createninja',methods=['POST'])
def create_ninja():
    data = {
        "dojo_id":request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age'],
    }
    Ninja.save(data)
    return redirect('/')


@app.route('/new_user')
def ninjas():
    all_dojos= Dojo.get_all()
    return render_template("new_user.html", all_dojos=all_dojos)

@app.route('/dojo_show/<int:id>')
def dojo_ninjas(id):
    data = {
        "id":id
    }
    ninjas_from= Ninja.get_from(data)
    return render_template("dojo_show.html", ninjas_from=ninjas_from)


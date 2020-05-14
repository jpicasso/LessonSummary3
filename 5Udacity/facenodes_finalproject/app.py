'''
----------------------------------------------------------------------------#
 IMPORTS
----------------------------------------------------------------------------#
'''

from flask import Flask, render_template, request, jsonify, redirect, url_for, request, abort
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
import ast

from .auth.auth import AuthError, requires_auth


'''
----------------------------------------------------------------------------#
 APP CONFIG
----------------------------------------------------------------------------#
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://johnpicasso:1234@localhost:5432/facenodes'
db = SQLAlchemy(app)
# setup_db(app)
CORS(app)



'''
----------------------------------------------------------------------------#
 MODELS
----------------------------------------------------------------------------#
'''

# Persons Class
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    picture = db.Column(db.String(500))
    notes = db.Column(db.String(500))
    user_id = db.Column(db.Integer)

class Group(db.Model):
    __tablename__ = 'group2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    user_id = db.Column(db.Integer)


class PersonGroup(db.Model):
    __tablename__ = 'persongroup'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

class User(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))


'''
-------------------------------------------------------------------
Groups Controllers
-------------------------------------------------------------------
'''

@app.route('/groups', methods=['POST'])
@requires_auth('post:groups')
def add_group(jwt):
   data = request.get_json()
   group = Group(name=data["name"], user_id=2)
   db.session.add(group)
   db.session.commit()
   
   return jsonify({ 
       'success': True,
       'id': group.id 
    })


@app.route('/groups/<group_id>', methods=['DELETE'])
@requires_auth('delete:groups')
def delete_group(jwt, group_id):
    Group.query.filter_by(id=group_id).delete()
    db.session.commit()
    return jsonify({ 'success': True })


@app.route('/groups/<group_id>', methods=['PATCH'])
@requires_auth('edit:groups')
def edit_groups(jwt, group_id):
    data = request.get_json()
    g = Group.query.get(group_id)
    g.name = data["name2"]
    db.session.commit()
    return jsonify({ 'success': True })


'''
-----------------------------------------------------------------
Persons Controllers
-----------------------------------------------------------------
'''

@app.route('/persons', methods=['POST'])
@requires_auth('post:persons')
def add_person(jwt):
    print('this worked')
    data = request.get_json()
    person = Person(name=data["name"], picture=data["picture"], notes=data["notes"],user_id=2)
    db.session.add(person)
    db.session.commit()

    person_group = PersonGroup(person_id=person.id, group_id=data["group_id"],user_id=2)
    db.session.add(person_group)
    db.session.commit()

    return jsonify({ 
       'success': True,
       'person_id': person.id, 
       'person_group_id': person_group.id
    })

@app.route('/persons/<person_id>', methods=['PATCH'])
@requires_auth('edit:persons')
def edit_person(jwt, person_id):
    data = request.get_json()
    p = Person.query.get(person_id)
    p.picture = data["picture"]
    p.name = data["name"]
    p.notes = data["notes"]
    db.session.commit()
    return jsonify({ 'success': True })


@app.route('/persons/<person_id>', methods=['DELETE'])
@requires_auth('delete:persons')
def deletePerson(jwt, person_id):
    Person.query.filter_by(id=person_id).delete()
    db.session.commit()
    return jsonify({ 'success': True })


'''
----------------------------------------------------------------
PersonGroup Controllers
----------------------------------------------------------------
'''

@app.route('/person_groups', methods=['POST'])
@requires_auth('post:person_groups')
def addPersonGroup(jwt):
    data = request.get_json()
    person_group = PersonGroup(person_id=data["person_id"], group_id=data["group_id"], user_id=2)
    db.session.add(person_group)
    db.session.commit()

    return jsonify({ 
       'success': True,
       'person_group_id': person_group.id
    })


@app.route('/person_groups/<person_group_id>', methods=['DELETE'])
@requires_auth('delete:person_groups')
def delete_person_group(jwt, person_group_id):
    PersonGroup.query.filter_by(id=person_group_id).delete()
    db.session.commit()
    return jsonify({ 'success': True })


''' 
------------------------------------------------------------------------
Setup pages.
------------------------------------------------------------------------
'''
@app.route('/loaddata', methods=['GET'])
@requires_auth('get:data')
def loaddata(jwt):
    user_id = 2
    users = User.query.all()
    groups = Group.query.filter_by(user_id=user_id)
    group_data =[]
    persons = Person.query.filter_by(user_id=user_id)
    person_data = []
    person_groups = PersonGroup.query.filter_by(user_id=user_id)
    person_group_data = []
    
    for u in users:
        if user_id == u.id:
            user = {"id": u.id, "name": u.name, "email": u.email}

    for g in groups:
        new_dictionary = {"id": g.id, "name": g.name}
        group_data.append(new_dictionary)

    for p in persons:
        new_dictionary = {"id": p.id, "name": p.name, "picture": p.picture, "notes": p.notes}
        person_data.append(new_dictionary)
    
    for x in person_groups:
        new_dictionary = {"id": x.id, "person_id": x.person_id, "group_id": x.group_id}
        person_group_data.append(new_dictionary)

    return jsonify({ 
        'success': True,
        'user': user,
        'groups': group_data,
        'persons': person_data,
        'person_groups': person_group_data,
    })


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/facecards')
def facecards():
    return render_template('FaceCards.html')

@app.route('/persons')
def facecardPeronsLoad():
    return render_template('FaceCardsPersons.html')

@app.route('/groups')
def loadgroups_page():
    return render_template('FaceCardsGroups.html')

@app.route('/edit_person')
def edit_person_page():
    return render_template('FaceCardsEditPerson.html')


@app.route('/logon')
def logon():
    return render_template('logonPage.html')


''' 
------------------------------------------------------------------------
Launch.
----------------------------------------------------------------------------
'''

db.create_all()

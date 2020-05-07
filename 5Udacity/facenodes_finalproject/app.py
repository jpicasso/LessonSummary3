'''
----------------------------------------------------------------------------#
 IMPORTS
----------------------------------------------------------------------------#
'''

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
----------------------------------------------------------------------------#
 APP CONFIG
----------------------------------------------------------------------------#
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://johnpicasso:1234@localhost:5432/facenodes'
db = SQLAlchemy(app)


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
    # user = db.Column(db.Integer(500), ForeignKey=True)


class Group(db.Model):
    __tablename__ = 'group2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))


class PersonGroup(db.Model):
    __tablename__ = 'persongroup'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)


'''
----------------------------------------------------------------------------#
 CONTROLLERs
----------------------------------------------------------------------------#
'''

'''
-------------------------------------------------------------------
Groups Controllers
-------------------------------------------------------------------
'''

@app.route('/groups', methods=['POST'])
def add_group():
   data = request.get_json()
   group = Group(name=data["name"])
   db.session.add(group)
   db.session.commit()
   
   return jsonify({ 
       'success': True,
       'id': group.id 
    })


@app.route('/groups/<group_id>', methods=['DELETE'])
def delete_group(group_id):
    Group.query.filter_by(id=group_id).delete()
    db.session.commit()
    return jsonify({ 'success': True })


@app.route('/groups/<group_id>', methods=['PATCH'])
def edit_groups(group_id):
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
def add_person():
    data = request.get_json()
    person = Person(name=data["name"], picture=data["picture"], notes=data["notes"])
    db.session.add(person)
    db.session.commit()

    person_group = PersonGroup(person_id=person.id, group_id=data["group_id"])
    db.session.add(person_group)
    db.session.commit()

    return jsonify({ 
       'success': True,
       'person_id': person.id, 
       'person_group_id': person_group.id
    })

@app.route('/persons/<person_id>', methods=['PATCH'])
def edit_person(person_id):
    data = request.get_json()
    p = Person.query.get(person_id)
    p.picture = data["picture"]
    p.name = data["name"]
    p.notes = data["notes"]
    db.session.commit()
    return jsonify({ 'success': True })


@app.route('/persons/<person_id>', methods=['DELETE'])
def deletePerson(person_id):
    Person.query.filter_by(id=person_id).delete()
    db.session.commit()
    return jsonify({ 'success': True })


'''
----------------------------------------------------------------
PersonGroup Controllers
----------------------------------------------------------------
'''

@app.route('/person_groups', methods=['POST'])
def addPersonGroup():
    data = request.get_json()
    person_group = PersonGroup(person_id=data["person_id"], group_id=data["group_id"])
    db.session.add(person_group)
    db.session.commit()

    return jsonify({ 
       'success': True,
       'person_group_id': person_group.id
    })


@app.route('/person_groups/<person_group_id>', methods=['DELETE'])
def delete_person_group(person_group_id):
    PersonGroup.query.filter_by(id=person_group_id).delete()
    db.session.commit()
    return jsonify({ 'success': True })


''' 
------------------------------------------------------------------------
Setup pages.
------------------------------------------------------------------------
'''

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

@app.route('/loaddata', methods=['GET'])
def loaddata():
    groups = Group.query.order_by('id').all()
    group_data =[]
    persons = Person.query.order_by('id').all()
    person_data = []
    person_groups = PersonGroup.query.order_by('id').all()
    person_group_data = []
    
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
        'groups': group_data,
        'persons': person_data,
        'person_groups': person_group_data,
    })

''' 
------------------------------------------------------------------------
Launch.
----------------------------------------------------------------------------
'''

db.create_all()

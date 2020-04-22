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


'''
----------------------------------------------------------------------------#
 CONTROLLERs
----------------------------------------------------------------------------#
'''

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/facecards')
def facecards():
    return render_template('FaceCards.html')


# @app.route('/playgame', methods=['GET'])
# def playgame():
#     persons = Person.query.all()
#     print(persons)

#     message = {'greeting':'Hello from Flask!'}
#     return jsonify(message)  



@app.route('/loaddata', methods=['GET'])
def loaddata():
    groups = Group.query.order_by('id').all()
    group_data =[]
    
    for g in groups:
        new_dictionary = {"id": g.id, "name": g.name}
        group_data.append(new_dictionary)

    return jsonify({ 
        'success': True,
        'groups': group_data
    })


'''
Groups Controllers
'''

@app.route('/groups')
def loadgroups_page():
    return render_template('FaceCardsGroups.html')


@app.route('/groups', methods=['POST'])
def addgroup():
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
    print(g)
    print(data)
    g.name = data["name2"]
    db.session.commit()
    return jsonify({ 'success': True })


'''
Persons Controllers
'''


''' 
------------------------------------------------------------------------
Launch.
----------------------------------------------------------------------------
'''

db.create_all()

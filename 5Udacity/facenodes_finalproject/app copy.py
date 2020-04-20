'''
----------------------------------------------------------------------------#
 IMPORTS
----------------------------------------------------------------------------#
'''

import json
import dateutil.parser
import babel
import time
import datetime
import os
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate



'''
----------------------------------------------------------------------------#
 APP CONFIG
----------------------------------------------------------------------------#
'''

app = Flask(__name__)             
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgres://johnpicasso:1234@localhost:5432/facenodes'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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

# Groups Class
class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    # user = db.Column(db.Integer(500), ForeignKey=True)
    

# Users Class
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

# PersonGroupsCross Class
# class PersonGroups(db.Model):
#     __tablename__ = 'persongroups'
#     id = db.Column(db.Integer, primary_key=True)
#     person_id = db.Column(db.Integer, ForeignKey=True)
#     group_id = db.Column(db.Integer, ForeignKey=True)


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


@app.route('/playgame', methods=['GET'])
def playgame():
    print('ran playgame')
    # persons = Person.query.order_by('id').all()
    persons = Person.query.all()
    print('hi')
    print (persons[1])

    # update local storage
'''
'/playgame' GET
- Purpose: loads one person from Persons table
- Input: previous person
- Output: new person
'''

@app.route('/groups', methods=['GET'])
def loadgroups():
    pass
'''
'/groups' GET
- Purpose: populates table of groups
- Input: None
- Output: all groups available to user
'''

@app.route('/groups', methods=['PATCH'])
def edit_groups():
    pass
'''
'/groups' PATCH
- Purpose: 
- Input: 
- Output: 
'''


@app.route('/groups', methods=['DELETE'])
def delete_group():
    pass
'''
'/groups' DELETE
- Purpose: 
- Input: 
- Output: 
'''


@app.route('/groups', methods=['POST'])
def add_group():
    pass
'''
'/groups' POST
- Purpose: 
- Input: 
- Output: 
'''

@app.route('/persons', methods=['GET'])
def load_persons():
    pass
'''
'/persons' GET
- Purpose: 
- Input: 
- Output: 
'''


@app.route('/persons', methods=['DELETE'])
def delete_persons():
    pass

'''
'/persons' DELETE
- Purpose: 
- Input: 
- Output: 
'''

@app.route('/persons', methods=['POST'])
def add_persons():
    pass
'''
'/persons' POST
- Purpose: 
- Input: 
- Output: 
'''

@app.route('/editPerson', methods=['GET'])
def get_person():
    pass
'''
'/editPerson' GET
- Purpose: 
- Input: 
- Output: 
'''


@app.route('/editPerson', methods=['PATCH'])
def edit_person():
    pass
'''
'/editPerson' PATCH
- Purpose: 
- Input: 
- Output: 
'''

@app.route('/editPerson', methods=['DELETE'])
def delete_person():
    pass
'''
'/editPerson' DELETE
- Purpose: 
- Input: 
- Output: 
'''

#----------------------------------------------------------------------------#
# Error Handlers.
#----------------------------------------------------------------------------#

# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('errors/404.html'), 404

# @app.errorhandler(500)
# def server_error(error):
#     return render_template('errors/500.html'), 500


# if not app.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('errors')

''' 
------------------------------------------------------------------------
Launch.
----------------------------------------------------------------------------
'''

# Default port:
if __name__ == '__main__':    #this runs the app
    app.run()

db.create_all()

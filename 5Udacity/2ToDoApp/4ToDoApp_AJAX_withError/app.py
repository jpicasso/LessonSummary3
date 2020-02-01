from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

# dialect = postgres1, username = johnpicasso, password = NA, host = local host, port = 5432, db name = todoapp
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://johnpicasso:1234@localhost:5432/todoapp'
db = SQLAlchemy(app)

# this is a Model in the MVC Pattern
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

# this route will take in user post requests 
@app.route('/todos/create', methods=['POST'])
def create_todo():
  error = False
  body = {}
  try:
    # import pdb; pdb.set_trace()
    description2 = request.get_json()['description']

    print("i am the description: " + description2)
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
    return jsonify(body)
  except:
    print("this is the body in except")
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if not error:
    print("we are not in error")
    return jsonify(body)
  
# this is a controller in the MVC Pattern
@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

db.create_all()

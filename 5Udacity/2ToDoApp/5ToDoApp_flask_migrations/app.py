from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# dialect = postgres1, username = johnpicasso, password = NA, host = local host, port = 5432, db name = todoapp
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://johnpicasso:1234@localhost:5432/todoapp'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# this is a Model in the MVC Pattern
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable = False, default = False)
    
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


# this route will take in user post requests 
@app.route('/todos/create', methods=['POST'])
def create_todo():
  description = request.get_json()['description']
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return jsonify ({
    'description': todo.description
  })
  
# this is a controller in the MVC Pattern
@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

db.create_all()

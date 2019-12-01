from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# dialect = postgres1, username = johnpicasso, password = NA, host = local host, port = 5432, db name = todoapp
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://johnpicasso@localhost:5432/todoapp'
db = SQLAlchemy(app)

# this is a Model in the MVC Pattern
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

# this is a controller in the MVC Pattern
@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
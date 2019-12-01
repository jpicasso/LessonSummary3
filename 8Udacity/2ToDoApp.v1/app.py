from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'To Do 1'
    }, {
        'description': 'To Do 2'
    }, {
        'description': 'To Do 3'
    }])
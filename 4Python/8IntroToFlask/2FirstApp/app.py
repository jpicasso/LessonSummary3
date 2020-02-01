#jsonify is used to convert strings to JSON and back and forth
# render_template is used in flask to pull up html files in your templates folder
# request ; note that this is different from requests
# Flask is a class in the flask library. It is used to let your python code talk to your html and js code
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

#this is JSON; JSON is not a dictionary but it is similar to a dictionary but is actually long string of text, and it gets converted to JSON using jsonify
# also note that JSON always uses double quotes

#note that this is a list, not a dictionary
stores = [
    {
        'name':'My Wonderful Store',
        'items': [
            {
                'name':'My Item',
                'price': 15.99
            }
        ]
    }
]

#each one of these @app.route is an endpoint that can be used as an API to talk back and forth to a database...and can be tested in Postman
@app.route('/')
def home():
    #flask automatically looks in the templates folder to find index.html so make sure your index.html file is in the templates folder
    return render_template('index.html')

#this needs you to import request
@app.route('/store', methods=['POST'])
def create_store():
    #this request is made to the /store endpoint and converts the JSON data into a python dictionary
    request_data = request.get_json()

    # this creates a new store
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    
    #this appends the new store to the list of stores
    stores.append(new_store)

    #this returns a string of JSON
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    #this iterates over stores and returns a string of JSON or an error message if no store is found
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    #note that this return only gets called if the above return never does get called
    return jsonify({'message':'store not found'})

@app.route('/store')
def get_stores():
    #jsonify only works on dictionaries so you need to make stores into a dictionary
    return jsonify({'stores':stores})

#this is a dynamic endpoint that will let user create items within different store names
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message': 'store not found'})

app.run(port=5000)

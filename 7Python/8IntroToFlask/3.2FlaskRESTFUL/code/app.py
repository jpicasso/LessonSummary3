from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
# this works with Resource and every resource has to be a Class
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


# defines our resource and in this case we only have one which is the Student
class Item(Resource):
    # note that there is no self here so make sure to use Item.parser later
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )

    # defines the methods that you can use on this endpoint; currently just get but could be post or others
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        # the above code is similar to the below code
        # this then decides what the method is going to do when this endpoint is called
        # for item in items:
        #     if item['name'] == name:
        #         # don't need to use jsonify because flask-RESTful does this for us
        #         return item

        # this returns a JSON item if you don't find a resource; 404 is the HTTP status code for Not Found
        # Note that 200 (everything is ok is most popular HTTP status code), 404 is second
        return {'item': item}, 200 if item is not None else 404

    def post(self,name):

        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists." .format(name)}, 400 # 400 is bad client request

        # data = request.get_json(silent=True) # silent = True returns none if the Header Content-Type is not included
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)

        # 201 is the HTTP status code for created and accepted; 202 is when the object is created but delayed
        # using the correct HTTP status code is important for debugging
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] !=name, items))
        return {'message': 'Item Deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}


# add resource in here, determine how it is accessed; note name parameter always goes to methods parameter as well

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)

# to try out this code make sure you run the app.py from the command line using $ python3 app.py
# then run it in postman using a GET request and the following endpoint http://127.0.0.1:5000/student/Rolf
# it should return { "student": "Rolf"

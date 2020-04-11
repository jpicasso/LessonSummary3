import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import ast

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
Uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()


@app.route('/drinks', methods=['GET'])
def get_drinks():
    '''
    public endpoint
    contains only the drink.short() data representation
    returns status code 200 and json {"success": True,
    "drinks": drinks} where drinks is the list of drinks in an
    array format or appropriate status code indicating reason for failure
    '''

    drinks = Drink.query.order_by('id').all()
    loaded_drinks = []
    for d in drinks:
        new_drink = d.short()
        loaded_drinks.append(new_drink)

    return jsonify({
        'success': True,
        'drinks': loaded_drinks,
    }), 200


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(jwt):
    '''
    it should require the 'get:drinks-detail' permission
    it should contain the drink.long() data representation
    returns status code 200 and json {"success": True,
    "drinks": drinks} where drinks is the list of drinks
    or appropriate status code indicating reason for failure
    '''

    try:
        drinks = Drink.query.order_by('id').all()
        loaded_drinks = []
        for d in drinks:
            recipe = ast.literal_eval(d.recipe)
            new_drink = {'id': d.id, 'title': d.title, 'recipe': recipe}
            loaded_drinks.append(new_drink)

        return jsonify({
                'success': True,
                'drinks': loaded_drinks,
            }), 200
    except:
        abort(422)


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drinks(jwt):
    '''
    it should create a new row in the drinks table
    it should require the 'post:drinks' permission
    it should contain the drink.long() data representation returns
    status code 200 and json {"success": True, "drinks": drink}
    where drink an array containing only the newly created drink
    or appropriate status code indicating reason for failure
    '''
    try:
        new_drink_id = 0
        drinks = Drink.query.order_by('id').all()
        if drinks != []:
            for d in drinks:
                new_drink_id = d.id + 1
        else:
            print('null')

        body = request.get_json()
        if body is None:
            abort(404)

        new_recipe = body.get('recipe')
        new_title = body.get('title')
        new_drink = Drink(
            id=new_drink_id,
            title=new_title,
            recipe=json.dumps(new_recipe)
        )
        new_drink.insert()

        return jsonify({
            'success': True,
            'drinks': new_drink.long()
        }), 200

    except:
        abort(422)


@app.route('/drinks/<drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drinks(jwt, drink_id):
    '''
    where <id> is the existing model id
    it should respond with a 404 error if <id> is not found
    it should update the corresponding row for <id>
    it should require the 'patch:drinks' permission
    it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks":
    drink} where drink an array containing only the updated drink
    or appropriate status code indicating reason for failure
    '''
    try:
        drink = Drink.query.get(drink_id)

        body = request.get_json()
        if body is None:
            abort(404)

        drink.title = body.get('title')
        drink.recipe = json.dumps(body.get('recipe'))
        drink.update()

        drink_array = []
        drink_array.append(drink.long())

        return jsonify({
                'success': True,
                'drinks': drink_array,
            }), 200

    except:
        abort(422)


@app.route('/drinks/<drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(jwt, drink_id):
    '''
    <drink_id> is the existing model id
    it should respond with a 404 error if <id> is not found
    it should delete the corresponding row for <id>
    it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True,
    "delete": id}  where id is the id of the deleted record
    or appropriate status code indicating reason for failure
    '''

    try:
        drink = Drink.query.get(drink_id)

        drink.delete()

        return jsonify({
            'success': True,
            'delete': drink_id,
        }), 200
    except:
        abort(422)


# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    '''
    Error handling for unprocessable entity
    '''
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def resource_not_found(error):
    '''
    Error handling for resource not found
    '''

    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(401)
def unauthorized(error):
    '''
    Error handling when user doesn't have permission
    '''

    return jsonify({
        "success": False,
        "error": 401,
        "message": "you are not authorized to do this!"
    }), 401


@app.errorhandler(400)
def bad_request(error):
    '''
    Error handling when something about the request was wrong
    and server couldn't handle it
    '''

    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request; something with it went wrong"
    }), 400


@app.errorhandler(500)
def internal_server_error(error):
    '''
    Catch all error handling
    '''

    return jsonify({
        "success": False,
        "error": 500,
        "message": "wtf...internal server errro"
    }), 500

'''
Expanle drink data format:

drinks = {
        1: {
            id: 1,
            title: 'matcha shake',
            recipe: [
                {
                    name: 'milk',
                    color: 'grey',
                    parts: 1
                },
                {
                    name: 'matcha',
                    color: 'green',
                    parts: 3
                },
                ]
        },
        2: {
            id: 2,
            title: 'flatwhite',
            recipe: [

                {
                    name: 'milk',
                    color: 'grey',
                    parts: 3
                },
                {
                    name: 'coffee',
                    color: 'brown',
                    parts: 1
                },
                ]
        },
        3: {
            id: 3,
            title: 'cap',
            recipe: [
                {
                    name: 'foam',
                    color: 'white',
                    parts: 1
                },
                {
                    name: 'milk',
                    color: 'grey',
                    parts: 2
                },
                {
                    name: 'coffee',
                    color: 'brown',
                    parts: 1
                },
                ]
        }
    };
'''

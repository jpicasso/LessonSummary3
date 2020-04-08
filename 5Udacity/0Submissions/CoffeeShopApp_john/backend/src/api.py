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

# uncomment below first time you run or to restart db
# db_drop_and_create_all()


@app.route('/drinks', methods=['GET'])
def get_drinks():
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
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "you are not authorized to do this!"
    }), 401


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "wtf...internal server errro"
    }), 500

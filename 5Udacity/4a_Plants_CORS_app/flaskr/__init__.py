from flask import Flask, request, jsonify, abort
from models import setup_db, Plant
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, PATCH, POST, DELETE, OPTIONS')
        return response
    
    @app.route('/plants')
    def get_plants():
        page = request.args.get('page', 1, type=int)
        start = (page -1 ) * 10
        end = start + 10
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]

        return jsonify({
            'success':True,
            'plants': formatted_plants[start:end],
            'total_plants': len(formatted_plants)
        })
    
    @app.route('/plants/<int:plant_id>')
    def get_specific_plant(plant_id):
        plant = Plant.query.filter(Plant.id == plant_id).one_or_none()

        if plant is None:
            abort(404)
        else:
            return jsonify({
                'success':True,
                'plant': plant.format()
            })

    @app.route('/plants/<int:plant_id>')
    def create_plant():
        body = request.get_json()



    @app.route('/plants/<int:plant_id>', methods = ['DELETE'])
    def delete_plant(plant_id):
        body = request.get_json()
        plant = Plant.query.filter(Plant.id == plant_id).one_or_none()



    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "unprocessable"
        }), 404


    return app
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

# this works with Resource and every resource has to be a Class
api = Api(app)


# defines our resource and in this case we only have one which is the Student
class Student(Resource):
    # defines the methods that you can use on this endpoint; currently just get but could be post or others
    def get(self,name):
        # this then decides what the method is going to do when this endpoint is called
        return {'student':name}


# add resource in here, determine how it is accessed; note name parameter always goes to methods parameter as well
api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)

# to try out this code make sure you run the app.py from the command line using $ python3 app.py
# then run it in postman using a GET request and the following endpoint http://127.0.0.1:5000/student/Rolf
# it should return { "student": "Rolf"
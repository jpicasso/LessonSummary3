from flask import Flask

# this is just boiler code to always be included
app = Flask(__name__)

# then add a decorater that acts on a method
@app.route('/') #this will impact the home page for example 'http://wwww.google.com/'
def home():
    return "Hello, World!!!"

#this runs the app and puts it on a local port 5000
app.run(port=5000)


#Code Explanation

# First we imported the Flask class. An instance of this class will be our WSGI application.
# Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.
# We then use the route() decorator to tell Flask what URL should trigger our function.
# The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
# Just save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.
# To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

# $ export FLASK_APP=hello.py
# $ flask run
#  * Running on http://127.0.0.1:5000/
terminal commands executed

$ dropdb todoapp
$ createdb todoapp
$ FLASK_APP=app.py flask run

to test to see if the error handling is working, go to line 24 of the app.py file and change the description to description2...then when you run the code, it should return an error

go to http://127.0.0.1:5000/ on your browswer to make sure that it is working


Presss command+shift+d to open a new CLI

$ psql todoapp

\dt
\d todos
 



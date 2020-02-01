terminal commands executed

$ dropdb todoapp
$ createdb todoapp
$ FLASK_APP=app.py FLASK_DEBUG=true flask run

Presss command+shift+d to open a new CLI

$ psql todoapp

>>> \dt
>>> \d todos
>>> 
INSERT INTO todos (description) VALUES ('Task 1');
INSERT INTO todos (description) VALUES ('Task 2');
INSERT INTO todos (description) VALUES ('Task 3');
INSERT INTO todos (description) VALUES ('Task 4');

go to http://127.0.0.1:5000/ on your browswer to make sure that it is working
Should see the 4 tasks in bullets and should be able to add new tasks
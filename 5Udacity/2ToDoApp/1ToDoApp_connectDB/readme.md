terminal commands executed

$ dropdb todoapp
$ createdb todoapp
$ FLASK_APP=app.py flask run

Presss command+shift+d to open a new CLI

$ psql todoapp

Note: if this doesn't work then exit out of the server...run the INSERT INTO SQL lines...then run FLASK_APP again...

INSERT INTO todos (description) VALUES ('Task 1');
INSERT INTO todos (description) VALUES ('Task 2');
INSERT INTO todos (description) VALUES ('Task 3');
INSERT INTO todos (description) VALUES ('Task 4');

go to http://127.0.0.1:5000/ on your browswer to make sure that it is working

It should have four bullets with Task 1, Task 2, Task 3, Task 4

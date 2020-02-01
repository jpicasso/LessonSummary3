delete migrations folder

terminal commands executed
$ dropdb todoapp
$ createdb todoapp
$ flask db init

$ pip3 install -r requirements.txt
$ FLASK_APP=app.py FLASK_DEBUG=true flask run

Presss command+shift+d to open a new CLI

$ psql todoapp

>>> \dt
>>> \d todos
>>> 
INSERT INTO todolists (name) VALUES ('Urgent');
INSERT INTO todolists (name) VALUES ('Follow up');
INSERT INTO todolists (name) VALUES ('Uncategorized');
INSERT INTO todos (description, completed, list_id) VALUES ('Task 1', True,1);
INSERT INTO todos (description, completed, list_id) VALUES ('Task 2',True,1);
INSERT INTO todos (description, completed, list_id) VALUES ('Task 3',False,1);
INSERT INTO todos (description, completed, list_id) VALUES ('Task 4',False,2);
INSERT INTO todos (description, completed, list_id) VALUES ('Task 5',False,2);

go to http://127.0.0.1:5000/ on your browswer to make sure that it is working
Should see the 4 tasks in bullets and should be able to add new tasks and check boxes

add a new task
check boxes as true or false
check to make sure it updated in the database by running the below code in the
delete a task

psql terminal
>>> SELECT * FROM todos;





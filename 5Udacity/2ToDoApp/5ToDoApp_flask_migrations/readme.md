
If you are coming from lesson 4 {
    - comment out the "completed" code line in the app.py file within the todo class
    - delete migrations folder
    $ flask db init
}

Skip below steps if you are coming from version 4 of the todo app
{
    $ dropdb todoapp
    $ createdb todoapp
    $ flask db init
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
}

take out the comment around the completed code in the app.py file within the Todo class. save file

$ flask db migrate

Go to the file in migrations/versions...then change the def upgrade()
- change nullable from false to true
- add in the below code below the op.add_column line to take the old data and insert false under the completed column
    - op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    - op.alter_column('todos', 'completed', nullable=False)

$ flask db upgrade

$ psql todoapp
>>> \dt
>>> \d todos
>>>
INSERT INTO todos (description, completed) VALUES ('Task 5', True);
INSERT INTO todos (description, completed) VALUES ('Task 6',True);
SELECT * FROM todos;

Should see the 6 tasks in bullets with task 5 and 6 showing true under completed




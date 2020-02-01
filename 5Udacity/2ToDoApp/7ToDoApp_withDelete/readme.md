If you are coming from Lesson 6 {
    $ FLASK_APP=app.py FLASK_DEBUG=true flask run
    go to http://127.0.0.1:5000/ on your browswer to make sure that it is working
}


if you are starting from scartch to this
{
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
    INSERT INTO todos (description, completed) VALUES ('Task 1', True);
    INSERT INTO todos (description, completed) VALUES ('Task 2',True);
    INSERT INTO todos (description, completed) VALUES ('Task 3',False);
    INSERT INTO todos (description, completed) VALUES ('Task 4',False);

    go to http://127.0.0.1:5000/ on your browswer to make sure that it is working
    Should see the 4 tasks in bullets and should be able to add new tasks and check boxes

    add a new task
    check boxes as true or false
    check to make sure it updated in the database by running the below code in the
    delete a task

    psql terminal
    >>> SELECT * FROM todos;
}




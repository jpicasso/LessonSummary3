# Facenodes Final Project

This app is a game that allows you to:

1) Remember names and facts about people based on their face in flash card format 
2) Group together people to remmember people in groups
3) Add / edit / delete people and groups
4) (extra) Search for a person based on a text query string.

### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── backend
  │   ├── app.py *** the main driver of the app 
  │   ├── models.py *** database schema which includes SQLAlchemy models.
  │   ├── requirements.txt *** dependencies  to install 
  │   ├── dummyfaces.psql *** initial database content
  ├── static
  │   ├── css 
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      ├── forms
      ├── layouts
      └── pages
  ```


### Development Setup

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```bash
  cd YOUR_PROJECT_DIRECTORY_PATH/
  virtualenv --no-site-packages venv
  source venv/bin/activate
  ```

2. Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. database set up (upfront only; or on resets)
terminal commands executed...don't run this in the virtual environment or it won't work
  ```bash
  dropdb facenodes
  createdb facenodes
  # delete migrations folder if it exists then initialize
  flask db init
  psql facenodes
  #\dt #check to make sure tables are there
  ```

4. Run the development server: 
  ```
  export FLASK_APP=app.py
  export FLASK_ENV=development
  python3 app.py
  ```

5. Navigate to Home page [http://localhost:5432]


## API Endpoints
'/playgame' GET
- Purpose: loads one person from Persons table
- Input: previous person
- Output: new person

'/groups' GET
- Purpose: populates table of groups
- Input: None
- Output: all groups available to user

'/groups' PATCH
- Purpose: 
- Input: 
- Output: 

'/groups' DELETE
- Purpose: 
- Input: 
- Output: 

'/groups' POST
- Purpose: 
- Input: 
- Output: 

'/persons' GET
- Purpose: 
- Input: 
- Output: 

'/persons' DELETE
- Purpose: 
- Input: 
- Output: 

'/persons' POST
- Purpose: 
- Input: 
- Output: 

'/editPerson' GET
- Purpose: 
- Input: 
- Output: 

'/editPerson' PATCH
- Purpose: 
- Input: 
- Output: 

'/editPerson' DELETE
- Purpose: 
- Input: 
- Output: 

# Full Stack API Final Project

## To start the project and the server...run this...

From the terminal...
navigate to the backend folder and enter:
```bash
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Open up a new terminal...
navigate to the frontend folder and enter:
```bash
npm install
npm start
```
Open [http://localhost:3000] to view it in the browser. The page will reload if you make edits.

## Database Setup (first time only or to reset the db)
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Testing
To run the tests, run the below...make sure to re run every line each time you want to test it
```bash
dropdb trivia_test && createdb trivia_test
psql trivia_test < trivia.psql 
python3 test_flaskr.py
```

## API Endpoints
GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Purpose: Gets list of paginated questions by category
- Request Arguments: None
- Returns: An object with a single key, categories, questions, current category, and number of questions. 

DELETE '/questions/<int:question_id>'
- Purpose: deletes a specific question
- Request Arguments: question id
- Returns: An object with a single key, id of question deleted, current paginated questions and number of questions.

POST '/questions'
- Purpose: creates a new question with answer, category listing, and difficulty
- Request Arguments: None
- Returns: JSON object with success being true or a 422 error

POST '/search'
- Purpose: allows you to search all questions that have the searchTerm from the user
- Request Arguments: None
- Returns: An object with a single key, question objects, and number of questions

GET '/categories/<int:category_id>'
- Purpose: retrieves all questions within a specific category
- Request Arguments: category id
- Returns: list of current questions and current categories and number of questions

POST '/quizzes'
- Purpose: generates 5 random questions from selected category
- Request Arguments: None
- Returns: list of previous questions, current questions, and the users guess

================================================================================
Graveyard 
================================================================================

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)
